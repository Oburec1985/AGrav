const logsNode = document.getElementById('logs');
const copyButton = document.getElementById('copy');
const clearButton = document.getElementById('clear');

const formatLogs = (logs) => JSON.stringify(logs || [], null, 2);

const render = () => {
  chrome.storage.local.get({ logs: [] }, ({ logs }) => {
    logsNode.textContent = logs.length ? formatLogs(logs) : 'Лог пуст. Открой видео и обнови страницу.';
  });
};

copyButton.addEventListener('click', async () => {
  chrome.storage.local.get({ logs: [] }, async ({ logs }) => {
    await navigator.clipboard.writeText(formatLogs(logs));
    copyButton.textContent = 'Скопировано';
    setTimeout(() => {
      copyButton.textContent = 'Скопировать лог';
    }, 1200);
  });
});

clearButton.addEventListener('click', () => {
  chrome.runtime.sendMessage({ source: 'yvac', type: 'clear-logs' }, render);
});

render();
