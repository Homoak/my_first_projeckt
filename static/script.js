        function play() {
          var audio = document.getElementById("audio");
          audio.currentTime = 0;
          audio.play();
        }
          const button = document.getElementById('soundButton');
          const hoverSound = document.getElementById('hoverSound');

          button.addEventListener('mouseenter', () => {
              hoverSound.currentTime = 0; // Возвращает звук к началу
              hoverSound.play();
          });
          function playSound() {
      var sound = document.getElementById("clickSound");
      sound.play();
  }

  document.addEventListener('DOMContentLoaded', () => {
      const links = document.querySelectorAll('a');
      const hoverSound = document.getElementById('hoverSound');

      links.forEach(link => {
          link.addEventListener('mouseover', () => {
              hoverSound.currentTime = 0;
              hoverSound.play();
          });
      });
  });
  function playSound() {
      var sound = document.getElementById("clickSound");
      sound.currentTime = 0;  // Встановлює початок відтворення з самого початку
      sound.play();
  }
        function toggleTheme() {
            document.body.classList.toggle('dark-theme');

            // Якщо активована темна тема, зберігаємо це в localStorage
            if (document.body.classList.contains('dark-theme')) {
                localStorage.setItem('theme', 'dark');
            } else {
                localStorage.setItem('theme', 'light');
            }
        }