// Football Strategy Club - mobile hamburger menu
(function () {
  document.addEventListener('DOMContentLoaded', function () {
    var toggle = document.querySelector('.nav-toggle');
    var nav = document.querySelector('.site-nav');
    if (!toggle || !nav) return;

    function closeNav() {
      nav.classList.remove('is-open');
      toggle.classList.remove('is-active');
      toggle.setAttribute('aria-expanded', 'false');
    }

    toggle.addEventListener('click', function () {
      var isOpen = nav.classList.toggle('is-open');
      toggle.classList.toggle('is-active', isOpen);
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', closeNav);
    });

    // collapse back to desktop layout without leaving the menu stuck open
    window.addEventListener('resize', function () {
      if (window.innerWidth > 640) closeNav();
    });
  });
})();

// Back to top button - fades out after 5s of scroll inactivity,
// fades back in as soon as scrolling resumes.
(function () {
  var HIDE_DELAY = 3000;

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.back-to-top').forEach(function (btn) {
      var hideTimer = null;

      function show() {
        btn.classList.remove('is-hidden');
      }

      function scheduleHide() {
        if (hideTimer) clearTimeout(hideTimer);
        hideTimer = setTimeout(function () {
          btn.classList.add('is-hidden');
        }, HIDE_DELAY);
      }

      btn.addEventListener('click', function () {
        window.scrollTo({ top: 0, behavior: 'smooth' });
        show();
        scheduleHide();
      });

      window.addEventListener('scroll', function () {
        show();
        scheduleHide();
      }, { passive: true });

      // start visible, then begin the inactivity countdown
      show();
      scheduleHide();
    });
  });
})();

// Diagram zoom modal - opens an enlarged copy of a diagram's SVG
(function () {
  document.addEventListener('DOMContentLoaded', function () {
    var modal = document.querySelector('.diagram-modal');
    var zoomButtons = document.querySelectorAll('.diagram-zoom-btn');
    if (!modal || !zoomButtons.length) return;

    var inner = modal.querySelector('.diagram-modal-inner');
    var closeBtn = modal.querySelector('.diagram-modal-close');
    var backdrop = modal.querySelector('.diagram-modal-backdrop');

    function openModal(svg) {
      inner.innerHTML = '';
      inner.appendChild(svg.cloneNode(true));
      modal.classList.add('is-open');
      modal.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    }

    function closeModal() {
      modal.classList.remove('is-open');
      modal.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
      inner.innerHTML = '';
    }

    zoomButtons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var box = btn.closest('.diagram-box');
        // ':scope > svg' targets only the diagram's own SVG (a direct
        // child of .diagram-box), not the small icon SVG nested inside
        // this button.
        var svg = box ? box.querySelector(':scope > svg') : null;
        if (svg) openModal(svg);
      });
    });

    closeBtn.addEventListener('click', closeModal);
    backdrop.addEventListener('click', closeModal);
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && modal.classList.contains('is-open')) closeModal();
    });
  });
})();

// Hashtag list truncation - if a .topic-tags block has more than LIMIT
// tags, hide the rest behind a "...すべて表示" link that reveals them on click.
(function () {
  var LIMIT = 10;

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.topic-tags').forEach(function (list) {
      var tags = Array.prototype.slice.call(list.querySelectorAll(':scope > a'));
      if (tags.length <= LIMIT) return;

      var hidden = tags.slice(LIMIT);
      hidden.forEach(function (a) {
        a.classList.add('tag-hidden');
      });

      var more = document.createElement('span');
      more.className = 'tag-more';
      more.appendChild(document.createTextNode('...'));
      var moreLink = document.createElement('a');
      moreLink.href = '#';
      moreLink.className = 'tag-more-label';
      moreLink.textContent = 'すべて表示';
      moreLink.addEventListener('click', function (e) {
        e.preventDefault();
        hidden.forEach(function (a) {
          a.classList.remove('tag-hidden');
        });
        more.remove();
      });
      more.appendChild(moreLink);

      tags[LIMIT - 1].insertAdjacentElement('afterend', more);
    });
  });
})();
