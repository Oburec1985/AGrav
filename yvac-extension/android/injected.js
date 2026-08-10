(() => {
  'use strict';

  const AD_MEDIA_PATTERN = /\/\/(?:(?:cdn\.)?lotory\.top|iwad\.cachefly\.net|assets\.ahmybid\.net|(?:[^/]+\.)?p0sembed\.com)\//i;
  const AD_TEXT_PATTERN = /реклама\s+закончится|пропустить|advertisement|skip\s+ad/i;

  document.documentElement.setAttribute('data-yvac-injected', '1');
  document.dispatchEvent(new CustomEvent('yvac:injected-ready', {
    detail: {
      href: location.href
    }
  }));

  const isBlockedMedia = (value) => AD_MEDIA_PATTERN.test(String(value || ''));

  const rememberBlocked = (value) => {
    document.documentElement.setAttribute('data-yvac-last-blocked-src', String(value || ''));
    document.dispatchEvent(new CustomEvent('yvac:injected-blocked-media', {
      detail: {
        href: location.href,
        src: String(value || '')
      }
    }));
  };

  const blockMediaElement = (media) => {
    if (!(media instanceof HTMLMediaElement)) {
      return false;
    }

    const mediaSrc = media.currentSrc || media.src || media.getAttribute('src') || '';
    const sourceSrc = Array.from(media.querySelectorAll('source'))
      .map((source) => source.src || source.getAttribute('src') || '')
      .find(isBlockedMedia) || '';
    const blockedSrc = isBlockedMedia(mediaSrc) ? mediaSrc : sourceSrc;

    if (!blockedSrc) {
      return false;
    }

    try {
      rememberBlocked(blockedSrc);
      media.pause();
      media.muted = true;
      media.removeAttribute('src');
      for (const source of media.querySelectorAll('source')) {
        if (isBlockedMedia(source.src || source.getAttribute('src'))) {
          source.removeAttribute('src');
        }
      }
      media.load();
      media.dispatchEvent(new Event('ended', { bubbles: true }));
      return true;
    } catch {
      return false;
    }
  };

  const patchSrcSetters = () => {
    const mediaDescriptor = Object.getOwnPropertyDescriptor(HTMLMediaElement.prototype, 'src');
    if (mediaDescriptor?.set && mediaDescriptor?.get) {
      Object.defineProperty(HTMLMediaElement.prototype, 'src', {
        configurable: true,
        enumerable: mediaDescriptor.enumerable,
        get: mediaDescriptor.get,
        set(value) {
          if (isBlockedMedia(value)) {
            rememberBlocked(value);
            this.pause();
            this.removeAttribute('src');
            this.dispatchEvent(new Event('ended', { bubbles: true }));
            return;
          }
          mediaDescriptor.set.call(this, value);
        }
      });
    }

    const sourceDescriptor = Object.getOwnPropertyDescriptor(HTMLSourceElement.prototype, 'src');
    if (sourceDescriptor?.set && sourceDescriptor?.get) {
      Object.defineProperty(HTMLSourceElement.prototype, 'src', {
        configurable: true,
        enumerable: sourceDescriptor.enumerable,
        get: sourceDescriptor.get,
        set(value) {
          if (isBlockedMedia(value)) {
            rememberBlocked(value);
            this.removeAttribute('src');
            this.parentElement?.dispatchEvent(new Event('ended', { bubbles: true }));
            return;
          }
          sourceDescriptor.set.call(this, value);
        }
      });
    }

    const originalSetAttribute = Element.prototype.setAttribute;
    Element.prototype.setAttribute = function patchedSetAttribute(name, value) {
      const isSrc = String(name).toLowerCase() === 'src';
      const isMediaNode = this instanceof HTMLMediaElement || this instanceof HTMLSourceElement;
      if (isSrc && isMediaNode && isBlockedMedia(value)) {
        rememberBlocked(value);
        this.removeAttribute('src');
        this.dispatchEvent(new Event('ended', { bubbles: true }));
        return;
      }
      return originalSetAttribute.call(this, name, value);
    };
  };

  const stripAdvertisingConfig = (config) => {
    if (!config || typeof config !== 'object') {
      return config;
    }

    if (Object.prototype.hasOwnProperty.call(config, 'advertising')) {
      delete config.advertising;
      document.documentElement.setAttribute('data-yvac-ad-config-removed', '1');
    }

    return config;
  };

  const wrapPlayer = (player) => {
    if (!player || player.__yvacWrapped) {
      return player;
    }

    try {
      const originalSetup = player.setup;
      if (typeof originalSetup === 'function') {
        player.setup = function wrappedSetup(config) {
          return originalSetup.call(this, stripAdvertisingConfig(config));
        };
      }
      player.__yvacWrapped = true;
    } catch {
      // Some player objects may be sealed.
    }

    return player;
  };

  const wrapJwplayer = (jwplayerFn) => {
    if (typeof jwplayerFn !== 'function' || jwplayerFn.__yvacWrapped) {
      return jwplayerFn;
    }

    const wrapped = function wrappedJwplayer(...args) {
      return wrapPlayer(jwplayerFn.apply(this, args));
    };

    for (const key of Object.keys(jwplayerFn)) {
      try {
        wrapped[key] = jwplayerFn[key];
      } catch {
        // Preserve what can be copied.
      }
    }

    wrapped.__yvacWrapped = true;
    return wrapped;
  };

  const patchJwplayerGlobal = () => {
    let storedJwplayer = typeof window.jwplayer === 'function'
      ? wrapJwplayer(window.jwplayer)
      : window.jwplayer;

    try {
      Object.defineProperty(window, 'jwplayer', {
        configurable: true,
        get() {
          return storedJwplayer;
        },
        set(value) {
          storedJwplayer = wrapJwplayer(value);
        }
      });
    } catch {
      if (typeof window.jwplayer === 'function') {
        window.jwplayer = wrapJwplayer(window.jwplayer);
      }
    }
  };

  const clickElement = (node) => {
    if (!node) {
      return;
    }

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
  };

  const trySkip = () => {
    try {
      if (typeof window.jwplayer === 'function') {
        for (const playerNode of document.querySelectorAll('.jwplayer[id]')) {
          const player = window.jwplayer(playerNode.id);
          if (player && typeof player.skipAd === 'function') {
            player.skipAd();
          }
        }
      }

      for (const media of document.querySelectorAll('video, audio')) {
        blockMediaElement(media);
      }

      for (const playerNode of document.querySelectorAll('.jwplayer, .jw-wrapper')) {
        const skipButton = playerNode.querySelector('.jw-skip.jw-skippable, [aria-label*="Пропустить" i]');
        if (skipButton) {
          clickElement(skipButton);
        }

        const video = playerNode.querySelector('video');
        const playerText = playerNode.textContent || '';
        if (!video || !AD_TEXT_PATTERN.test(playerText)) {
          continue;
        }

        if (!blockMediaElement(video)) {
          video.muted = true;
          video.playbackRate = 16;
          if (Number.isFinite(video.duration) && video.duration > 0) {
            video.currentTime = Math.max(video.currentTime, video.duration - 0.1);
          } else {
            video.currentTime += 1;
          }
        }
      }
    } catch {
      // Keep the page script silent.
    }
  };

  patchSrcSetters();
  patchJwplayerGlobal();
  window.setInterval(trySkip, 100);
  document.addEventListener('yvac:skip-ad', trySkip);
  trySkip();
})();
