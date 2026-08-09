(() => {
  'use strict';

  const VERSION = 'android-1.0.0';
  const MAX_LOGS = 200;

  const logEvent = (type, data = {}) => {
    const entry = {
      time: new Date().toLocaleTimeString(),
      version: VERSION,
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

  chrome.runtime.onInstalled.addListener(() => {
    logEvent('installed');
  });

  chrome.runtime.onStartup?.addListener(() => {
    logEvent('startup');
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
