(function () {
  function initMenu() {
    var burger = document.getElementById('burger');
    var nav = document.getElementById('nav');
    if (burger && nav) {
      burger.addEventListener('click', function () { nav.classList.toggle('open'); });
    }
  }

  function preselectService(form) {
    var m = /[?&]service=([a-z0-9-]+)/.exec(window.location.search);
    if (!m) return;
    var opt = form.querySelector('option[data-slug="' + m[1] + '"]');
    if (opt) opt.selected = true;
  }

  function fallbackMessage(form, detail) {
    var phone = form.getAttribute('data-phone');
    var tel = form.getAttribute('data-tel');
    var email = form.getAttribute('data-email');
    var safe = detail ? String(detail).replace(/[<>&"']/g, '') : '';
    var lead = safe ? safe + ' ' : "We couldn't send your request right now. ";
    return lead + 'Please call or text <a href="tel:' + tel + '">' + phone + '</a> or email <a href="mailto:' +
      email + '">' + email + '</a> and we\'ll get right back to you with your free estimate.';
  }

  function initForm() {
    var form = document.getElementById('estimate-form');
    if (!form) return;
    preselectService(form);
    var page = form.querySelector('input[name="page"]');
    if (page) page.value = window.location.href.split('#')[0];
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = form.querySelector('button[type="submit"]');
      var status = document.getElementById('form-status');
      var label = btn.textContent;
      btn.disabled = true;
      btn.textContent = 'Sending...';
      status.className = 'form-status';
      status.innerHTML = '';
      fetch(form.action, { method: 'POST', body: new FormData(form), headers: { 'Accept': 'application/json' } })
        .then(function (r) {
          return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok && j.ok, j: j }; });
        })
        .then(function (res) {
          if (res.ok) { window.location.href = 'thank-you.html'; return; }
          var err = new Error('send failed');
          err.userMsg = res.j && res.j.error;
          throw err;
        })
        .catch(function (err) {
          btn.disabled = false;
          btn.textContent = label;
          status.className = 'form-status error';
          status.innerHTML = fallbackMessage(form, err && err.userMsg);
        });
    });
  }

  function trackLead() {
    if (document.querySelector('[data-lead]') && typeof window.gtag === 'function') {
      window.gtag('event', 'generate_lead', { form_name: 'estimate' });
    }
  }

  function trackCalls() {
    document.addEventListener('click', function (e) {
      var a = e.target.closest ? e.target.closest('a[href^="tel:"]') : null;
      if (a && typeof window.gtag === 'function') {
        window.gtag('event', 'click_to_call', { link_url: a.getAttribute('href'), page_path: window.location.pathname });
      }
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    initMenu();
    initForm();
    trackLead();
    trackCalls();
  });
})();
