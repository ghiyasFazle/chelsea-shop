function showToast(message, type = "info", opts = {}) {
  const container = document.getElementById("toast-container");
  if (!container) return;

  const ttl = opts.ttl || 4000;

  const toast = document.createElement("div");
  toast.className = `toast toast--${type}`;
  toast.setAttribute('role','status');
  toast.setAttribute('aria-live','polite');

  const icon = document.createElement('div');
  icon.className = 'toast-icon';
  icon.innerText = (type === 'success') ? '✔' : (type === 'error') ? '✖' : (type === 'warning') ? '⚠' : 'ℹ';

  const body = document.createElement('div');
  body.className = 'toast-body';
  body.textContent = message;

  const close = document.createElement('button');
  close.className = 'toast-close';
  close.setAttribute('aria-label','Close notification');
  close.innerText = '×';

  close.addEventListener('click', () => {
    dismiss();
  });

  toast.appendChild(icon);
  toast.appendChild(body);
  toast.appendChild(close);

  container.appendChild(toast);

  // auto-dismiss with pause-on-hover
  let removed = false;
  let timeoutId = setTimeout(() => dismiss(), ttl);

  function dismiss(){
    if(removed) return; removed = true;
    toast.style.animation = 'toastOut 250ms ease forwards';
    setTimeout(()=> toast.remove(), 260);
  }

  toast.addEventListener('mouseenter', function(){
    clearTimeout(timeoutId);
  });
  toast.addEventListener('mouseleave', function(){
    timeoutId = setTimeout(() => dismiss(), 1500);
  });

  return { dismiss };
}
