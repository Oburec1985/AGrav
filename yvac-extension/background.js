(() => {
  'use strict';

  const VERSION = '1.0.2';

  const BLOCKED_URLS = [
    '*://lotory.top/*',
    '*://*.lotory.top/*',
    '*://p0sembed.com/*',
    '*://*.p0sembed.com/*',
    '*://*.ahmybid.net/*',
    '*://iwad.cachefly.net/*',
    '*://*.adfox.ru/*',
    '*://*.yandexadexchange.net/*',
    '*://nmcorp.video/static/players/*/vast.js',
    '*://*.nmcorp.video/static/players/*/vast.js'
  ];

  const BLOCKED_URL_PATTERN = /\/\/(?:(?:cdn\.)?lotory\.top|iwad\.cachefly\.net|(?:[^/]+\.)?p0sembed\.com|assets\.ahmybid\.net)\//i;

  const BLOCKED_TYPES = [
    'script',
    'xmlhttprequest',
    'sub_frame',
    'image',
    'media',
    'object',
    'other'
  ];

  const TARGET_HOSTS = [
    'yandex.ru',
    'yastatic.net',
    'nmcorp.video',
    'semyana.top',
    'semyana.com',
    'pornoembed.info',
    'porno-erotic.com'
  ];

  const WATCHED_MEDIA_URLS = [
    '*://*.lotory.top/*',
    '*://*.ahmybid.net/*',
    '*://iwad.cachefly.net/*',
    '*://*.p0sembed.com/*',
    '*://pornoembed.info/*',
    '*://*.pornoembed.info/*',
    '*://porno-erotic.com/*',
    '*://*.porno-erotic.com/*',
    '*://*.nmcorp.video/*',
    '*://*.semyana.top/*',
    '*://semyana.top/*',
    '*://*.semyana.com/*',
    '*://*.noodlemagazine.com/*',
    '*://video-preview.s3.yandex.net/*'
  ];

  const MAX_LOGS = 200;

  const logEvent = (type, data = {}) => {
    const entry = {
      time: new Date().toLocaleTimeString(),
      ...data,
      type
    };

    chrome.storage.local.get({ logs: [] }, ({ logs }) => {
      logs.push(entry);
      if (logs.length > MAX_LOGS) {
        logs = logs.slice(logs.length - MAX_LOGS);
      }
      chrome.storage.local.set({ logs });
    });
  };

  logEvent('background-started', {
    version: VERSION
  });

  const shouldBlockRequest = (url) => BLOCKED_URL_PATTERN.test(String(url || ''));

  const isTargetFrame = (url) => {
    try {
      const parsed = new URL(url);
      const host = parsed.hostname;
      return ((host === 'yandex.ru' || host.endsWith('.yandex.ru')) && parsed.pathname.startsWith('/video/'))
        || host === 'nmcorp.video'
        || host.endsWith('.nmcorp.video')
        || host === 'semyana.top'
        || host.endsWith('.semyana.top')
        || host === 'semyana.com'
        || host.endsWith('.semyana.com')
        || ((host === 'yastatic.net' || host.endsWith('.yastatic.net')) && parsed.pathname.startsWith('/video-player/'));
    } catch {
      return false;
    }
  };

  const ignoreLastError = () => {
    void chrome.runtime.lastError;
  };

  const injectIntoFrame = (tabId, frameId) => {
    chrome.tabs.insertCSS(tabId, {
      file: 'styles.css',
      frameId,
      runAt: 'document_start'
    }, () => {
      if (chrome.runtime.lastError) {
        logEvent('css-error', { tabId, frameId, error: chrome.runtime.lastError.message });
      }
    });

    chrome.tabs.executeScript(tabId, {
      file: 'content.js',
      frameId,
      runAt: 'document_start'
    }, () => {
      if (chrome.runtime.lastError) {
        logEvent('script-error', { tabId, frameId, error: chrome.runtime.lastError.message });
        return;
      }
      logEvent('script-injected', { tabId, frameId });
    });
  };

  const blockRequest = (details) => {
    if (!shouldBlockRequest(details.url)) {
      return {};
    }

    logEvent('blocked-request', {
      version: VERSION,
      url: details.url,
      requestType: details.type,
      tabId: details.tabId,
      frameId: details.frameId
    });
    return { cancel: true };
  };

  try {
    chrome.webRequest.onBeforeRequest.addListener(
      blockRequest,
      {
        urls: ['<all_urls>'],
        types: BLOCKED_TYPES
      },
      ['blocking']
    );
  } catch (error) {
    logEvent('blocking-listener-error', {
      version: VERSION,
      error: String(error?.message || error)
    });
  }

  chrome.webRequest.onBeforeRequest.addListener(
    (details) => {
      if (shouldBlockRequest(details.url)) {
        return;
      }

      logEvent('blocked-request', {
        version: VERSION,
        url: details.url,
        requestType: details.type,
        tabId: details.tabId,
        frameId: details.frameId
      });
      return { cancel: true };
    },
    {
      urls: BLOCKED_URLS,
      types: BLOCKED_TYPES
    },
    ['blocking']
  );

  chrome.webRequest.onBeforeRequest.addListener(
    (details) => {
      logEvent('media-request', {
        version: VERSION,
        url: details.url,
        requestType: details.type,
        tabId: details.tabId,
        frameId: details.frameId
      });
    },
    {
      urls: WATCHED_MEDIA_URLS,
      types: ['media', 'xmlhttprequest', 'other']
    }
  );

  chrome.webNavigation.onCommitted.addListener((details) => {
    if (details.tabId < 0 || !isTargetFrame(details.url)) {
      return;
    }

    logEvent('frame-committed', {
      url: details.url,
      tabId: details.tabId,
      frameId: details.frameId
    });
    injectIntoFrame(details.tabId, details.frameId);
  }, {
    url: TARGET_HOSTS.map((hostSuffix) => ({ hostSuffix }))
  });

  chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status !== 'complete' || !tab.url || !isTargetFrame(tab.url)) {
      return;
    }

    chrome.tabs.insertCSS(tabId, {
      file: 'styles.css',
      allFrames: true,
      runAt: 'document_start'
    }, ignoreLastError);

    chrome.tabs.executeScript(tabId, {
      file: 'content.js',
      allFrames: true,
      runAt: 'document_start'
    }, ignoreLastError);
  });

  chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (!message || message.source !== 'yvac') {
      return false;
    }

    if (message.type === 'clear-logs') {
      chrome.storage.local.set({ logs: [] }, () => sendResponse({ ok: true }));
      return true;
    }

    logEvent(message.type || 'message', {
      url: sender?.url,
      tabId: sender?.tab?.id,
      frameId: sender?.frameId,
      ...message.data
    });
    return false;
  });
})();
