(() => {
  'use strict';

  const BLOCKED_URLS = [
    '*://lotory.top/*',
    '*://*.lotory.top/*',
    '*://*.adfox.ru/*',
    '*://*.yandexadexchange.net/*',
    '*://nmcorp.video/static/players/*/vast.js',
    '*://*.nmcorp.video/static/players/*/vast.js'
  ];

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
    'nmcorp.video'
  ];

  const isTargetFrame = (url) => {
    try {
      const parsed = new URL(url);
      const host = parsed.hostname;
      return ((host === 'yandex.ru' || host.endsWith('.yandex.ru')) && parsed.pathname.startsWith('/video/'))
        || host === 'nmcorp.video'
        || host.endsWith('.nmcorp.video')
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
    }, ignoreLastError);

    chrome.tabs.executeScript(tabId, {
      file: 'content.js',
      frameId,
      runAt: 'document_start'
    }, ignoreLastError);
  };

  chrome.webRequest.onBeforeRequest.addListener(
    () => ({ cancel: true }),
    {
      urls: BLOCKED_URLS,
      types: BLOCKED_TYPES
    },
    ['blocking']
  );

  chrome.webNavigation.onCommitted.addListener((details) => {
    if (details.tabId < 0 || !isTargetFrame(details.url)) {
      return;
    }

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
})();
