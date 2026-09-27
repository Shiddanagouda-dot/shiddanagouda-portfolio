(function () {
  "use strict";

  // --- Active section highlighting for top navbar and mobile menu links ---
  var navLinks = document.querySelectorAll("header nav a[href^='#'], .mobile-menu a[href^='#']");
  var sections = [];
  
  navLinks.forEach(function (link) {
    var href = link.getAttribute("href");
    if (href && href.startsWith("#") && href.length > 1) {
      var id = href.substring(1);
      var section = document.getElementById(id);
      if (section) {
        sections.push({ id: id, el: section, link: link });
      }
    }
  });

  if (sections.length && "IntersectionObserver" in window) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          var match = sections.find(function (s) { return s.el === entry.target; });
          if (!match) return;
          if (entry.isIntersecting) {
            navLinks.forEach(function (l) { l.classList.remove("active", "text-cyan-400"); });
            // Highlight all links pointing to this section (desktop & mobile menu)
            sections.filter(function (s) { return s.id === match.id; }).forEach(function (s) {
              s.link.classList.add("active", "text-cyan-400");
            });
          }
        });
      },
      { rootMargin: "-30% 0px -60% 0px", threshold: 0 }
    );
    sections.forEach(function (s) { observer.observe(s.el); });
  }

  // --- Mobile menu toggle ---
  var toggle = document.getElementById("mobileToggle");
  var menu = document.getElementById("mobileMenu");
  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      var isOpen = menu.classList.toggle("open");
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });
    menu.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        menu.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }
})();