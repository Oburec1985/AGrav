(() => {
  'use strict';

  const BLOCK_WORDS = [
    'adfox',
    'advert',
    'advertisement',
    'banner',
    'commercial',
    'direct',
    'lotory',
    'promo',
    'реклам'
  ];

  const SAFE_WORDS = [
    'video',
    'player',
    'serp',
    'search',
    'content',
    'organic'
  ];

  const CANDIDATE_SELECTOR = [
    '[data-ad]',
    '[data-advert]',
    '[data-adfox]',
    '.DirectInlineContainer',
    '.VideoViewer-Direct',
    '.VideoViewer-DirectSkeleton',
    '.VideoViewer-VideoListPageDirect',
    '.VideoViewer-VideoListDirectSkeleton',
    '[id]',
    '[class]',
    '[aria-label]',
    '[title]',
    'iframe',
    'aside'
  ].join(',');

  const JW_SKIP_SELECTOR = [
    '.jw-skip',
    '.jw-skiptext',
    '[aria-label="Пропустить"]',
    '[aria-label*="Пропустить" i]',
    '[class*="skip" i]'
  ].join(',');

  const AD_TEXT_PATTERN = /реклама\s+закончится|пропустить|advertisement|skip\s+ad/i;
  const COUNTDOWN_PATTERN = /реклама\s+закончится\s+через|ad\s+will\s+end|skip\s+in/i;
  const AD_MEDIA_PATTERN = /\/\/(?:(?:cdn\.)?lotory\.top|iwad\.cachefly\.net|assets\.ahmybid\.net|(?:[^/]+\.)?p0sembed\.com)\//i;

  const sendLog = (type, data = {}) => {
    try {
      chrome.runtime.sendMessage({
        source: 'yvac',
        type,
        data
      });
    } catch {
      // Logging is diagnostic only.
    }
  };

  const injectPageScript = () => {
    document.documentElement.setAttribute('data-yvac-content', '1');

    if (document.documentElement.hasAttribute('data-yvac-page-script')) {
      return;
    }

    try {
      const script = document.createElement('script');
      script.src = chrome.runtime.getURL('injected.js');
      script.async = false;
      script.onload = () => {
        sendLog('page-script-loaded', { href: location.href });
        script.remove();
      };
      script.onerror = () => {
        sendLog('page-script-error', { href: location.href });
        script.remove();
      };
      (document.documentElement || document.head || document).appendChild(script);
      document.documentElement.setAttribute('data-yvac-page-script', '1');
      sendLog('page-script-added', { href: location.href });
    } catch {
      // Some sandboxed frames can reject extension URLs; isolated-world cleanup still runs.
    }
  };

  const patchYastaticSandbox = () => {
    if (!location.hostname.endsWith('yastatic.net')) {
      return;
    }

    document.documentElement.setAttribute('data-yvac-yastatic-frame', '1');
  };

  const normalized = (value) => String(value || '').toLowerCase();

  const containsBlockWord = (value) => {
    const text = normalized(value);
    return BLOCK_WORDS.some((word) => text.includes(word));
  };

  const containsSafeWord = (value) => {
    const text = normalized(value);
    return SAFE_WORDS.some((word) => text.includes(word));
  };

  const markHidden = (node) => {
    node.setAttribute('data-yvac-hidden', '1');
    node.style.setProperty('display', 'none', 'important');
    node.style.setProperty('visibility', 'hidden', 'important');
    node.style.setProperty('pointer-events', 'none', 'important');
  };

  const shouldHide = (node) => {
    if (!(node instanceof HTMLElement)) {
      return false;
    }

    if (node.matches('.DirectInlineContainer, .VideoViewer-Direct, .VideoViewer-DirectSkeleton, .VideoViewer-VideoListPageDirect, .VideoViewer-VideoListDirectSkeleton')) {
      return true;
    }

    if (node.matches('video, main, body, html')) {
      return false;
    }

    const signal = [
      node.id,
      node.className,
      node.getAttribute('data-ad'),
      node.getAttribute('data-advert'),
      node.getAttribute('data-adfox'),
      node.getAttribute('aria-label'),
      node.getAttribute('title'),
      node instanceof HTMLIFrameElement ? node.src : ''
    ].join(' ');

    if (!containsBlockWord(signal)) {
      return false;
    }

    const role = [
      node.getAttribute('role'),
      node.getAttribute('data-testid'),
      node.getAttribute('data-zone-name')
    ].join(' ');

    return !containsSafeWord(role);
  };

  const cleanRoot = (root) => {
    if (!(root instanceof Document || root instanceof HTMLElement || root instanceof DocumentFragment)) {
      return;
    }

    const candidates = root.querySelectorAll(CANDIDATE_SELECTOR);
    for (const node of candidates) {
      if (shouldHide(node)) {
        markHidden(node);
      }
    }
  };

  const clickElement = (node) => {
    if (typeof node.click === 'function') {
      node.click();
    }

    for (const eventType of ['pointerdown', 'mousedown', 'mouseup', 'click']) {
      const EventCtor = eventType.startsWith('pointer') && typeof PointerEvent === 'function'
        ? PointerEvent
        : MouseEvent;

      node.dispatchEvent(new EventCtor(eventType, {
        bubbles: true,
        cancelable: true,
        view: window
      }));
    }

    for (const eventType of ['keydown', 'keyup']) {
      node.dispatchEvent(new KeyboardEvent(eventType, {
        bubbles: true,
        cancelable: true,
        key: 'Enter',
        code: 'Enter'
      }));
    }
  };

  const skipJwPlayerAd = () => {
    document.dispatchEvent(new CustomEvent('yvac:skip-ad'));

    const skipButtons = document.querySelectorAll(JW_SKIP_SELECTOR);
    for (const button of skipButtons) {
      const text = normalized(button.textContent);
      const label = normalized(button.getAttribute('aria-label'));

      if (!text.includes('пропустить') && !label.includes('пропустить') && !text.includes('skip')) {
        continue;
      }

      const clickable = button.closest('[role="button"], button, .jw-skip') || button;
      const isUnlocked = clickable.classList.contains('jw-skippable')
        || button.classList.contains('jw-skippable')
        || !normalized(clickable.textContent).includes('через');

      if (isUnlocked) {
        sendLog('skip-click', { href: location.href });
        clickElement(clickable);
      }
    }

    const players = document.querySelectorAll('.jwplayer, .jw-wrapper, [class*="jwplayer" i], [id*="jwplayer" i]');
    for (const player of players) {
      const playerText = player.textContent || '';
      const video = player.querySelector('video');
      const videoSrc = video?.currentSrc || video?.src || '';
      const isAd = AD_TEXT_PATTERN.test(playerText)
        || COUNTDOWN_PATTERN.test(playerText)
        || player.classList.contains('jw-flag-ads')
        || Boolean(player.querySelector('#player_box_vast, .jw-plugin-vast'))
        || AD_MEDIA_PATTERN.test(videoSrc);

      if (!isAd) {
        continue;
      }

      if (!video) {
        continue;
      }

      try {
        sendLog('jw-ad-state', {
          href: location.href,
          src: videoSrc,
          text: playerText.slice(0, 160),
          className: player.className
        });
        video.muted = true;
        video.playbackRate = 16;
        if (Number.isFinite(video.duration) && video.duration > 0) {
          video.currentTime = Math.max(video.currentTime, video.duration - 0.2);
        } else if (COUNTDOWN_PATTERN.test(playerText)) {
          video.currentTime += 0.75;
        }

        if (AD_MEDIA_PATTERN.test(videoSrc)) {
          sendLog('blocked-media-element', { src: videoSrc, href: location.href });
          video.pause();
          video.removeAttribute('src');
          video.load();
        }
      } catch {
        // JWPlayer can block direct media control, so button clicking remains the main path.
      }
    }
  };

  const skipAdVideo = () => {
    const videos = document.querySelectorAll('video');
    for (const video of videos) {
      const wrapperText = normalized(video.closest('[class], [id]')?.outerHTML || '');
      const videoSrc = video.currentSrc || video.src || '';
      if (!containsBlockWord(wrapperText) && !AD_MEDIA_PATTERN.test(videoSrc)) {
        continue;
      }

      try {
        video.muted = true;
        if (Number.isFinite(video.duration) && video.duration > 0) {
          video.currentTime = Math.max(video.currentTime, video.duration - 0.2);
        }
        if (AD_MEDIA_PATTERN.test(videoSrc)) {
          sendLog('blocked-media-element', { src: videoSrc, href: location.href });
          video.pause();
          video.removeAttribute('src');
          video.load();
        }
      } catch {
        // Some embedded players disallow seeking. Network and CSS rules still handle most cases.
      }
    }
  };

  const clean = () => {
    document.documentElement.classList.add('yvac-enabled');
    document.body?.classList.add('yvac-cleaning');
    injectPageScript();
    patchYastaticSandbox();
    cleanRoot(document);
    skipJwPlayerAd();
    skipAdVideo();
  };

  document.addEventListener('yvac:injected-ready', (event) => {
    sendLog('injected-ready', event.detail || {});
  });

  document.addEventListener('yvac:injected-blocked-media', (event) => {
    sendLog('injected-blocked-media', event.detail || {});
  });

  const reportState = () => {
    const videos = Array.from(document.querySelectorAll('video'))
      .map((video) => video.currentSrc || video.src)
      .filter(Boolean);
    const iframes = Array.from(document.querySelectorAll('iframe'))
      .map((iframe) => iframe.src || iframe.getAttribute('src') || '')
      .filter(Boolean);

    if (videos.length || iframes.length || /(?:nmcorp|yastatic|semyana|pornoembed)/i.test(location.hostname)) {
      sendLog('frame-state', {
        extensionVersion: chrome.runtime.getManifest().version,
        href: location.href,
        videos,
        iframes,
        injected: document.documentElement.getAttribute('data-yvac-injected'),
        content: document.documentElement.getAttribute('data-yvac-content'),
        pageScript: document.documentElement.getAttribute('data-yvac-page-script'),
        playerClass: document.querySelector('#player_box')?.className || '',
        adText: document.querySelector('.jw-text-alt')?.textContent || ''
      });
    }
  };

  const observer = new MutationObserver((mutations) => {
    for (const mutation of mutations) {
      for (const node of mutation.addedNodes) {
        if (node instanceof HTMLElement || node instanceof DocumentFragment) {
          cleanRoot(node);
        }
      }
    }
    skipJwPlayerAd();
    skipAdVideo();
  });

  const start = () => {
    clean();
    observer.observe(document.documentElement, {
      childList: true,
      subtree: true
    });
    window.setInterval(skipJwPlayerAd, 100);
    window.setInterval(clean, 1500);
    window.setInterval(reportState, 3000);
    reportState();
  };

  if (document.readyState === 'loading') {
    injectPageScript();
    document.addEventListener('DOMContentLoaded', start, { once: true });
  } else {
    start();
  }
})();
