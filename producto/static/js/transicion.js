<script>
  document.addEventListener("DOMContentLoaded", function () {
    document.body.style.opacity = 1;

    document.querySelectorAll('a[href^="/"]').forEach(function (anchor) {
      anchor.addEventListener("click", function (e) {
        e.preventDefault();

        const href = this.getAttribute("href");

        document.body.classList.add("fade-out");

        setTimeout(function () {
          window.location.href = href;
        }, 500);
      });
    });
  });
</script>