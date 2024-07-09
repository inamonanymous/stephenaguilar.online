document.addEventListener('DOMContentLoaded', function() {
  //header hide drop when scrolled 
  function closeDropdown()  {
    var dropdown = document.getElementById("dropdown-menu");
    document.getElementById('exitSvg').style.display = 'none';
    document.getElementById('hamSvg').style.display = 'block';
    dropdown.classList.remove("show-dropdown");
  }
  

  //header drop when scroll
    const header = document.getElementById('header');
    let scrolled = false;
  
    function handleScroll() {
      if (window.scrollY > 40 && !scrolled) {
        header.classList.add('scrolled');
        scrolled = true;
      } else if (window.scrollY <= 40 && scrolled) {
        header.classList.remove('scrolled');
        scrolled = false;
      }
    }
    window.addEventListener('scroll', handleScroll);
    window.addEventListener('scroll', closeDropdown);

  //loading screen
    const loadingScreen = document.getElementById('loading-screen');
    const mainElements = document.querySelectorAll('header, section, footer');

    window.addEventListener('load', function() {
        loadingScreen.style.opacity = '0';
        loadingScreen.style.zIndex = '-1';
        mainElements.forEach(function(element) {
            element.style.opacity = '1';
        });
    });

  //navbar 
  document.getElementById("hamburger").addEventListener("click", function() {
    var dropdown = document.getElementById("dropdown-menu");
      if (dropdown.classList.contains("show-dropdown")) {
        document.getElementById('exitSvg').style.display = 'none';
        document.getElementById('hamSvg').style.display = 'block';
        dropdown.classList.remove("show-dropdown");
      } else {
        document.getElementById('exitSvg').style.display = 'block';
        document.getElementById('hamSvg').style.display = 'none';
        dropdown.classList.add("show-dropdown");
    }
});


});
function scrollToSection(sectionId) {
  const section = document.getElementById(sectionId);
  if (section) {
    section.scrollIntoView({ behavior: 'smooth' });
  }
}
const validateEmail = (email) => {
  // Regular expression for validating email format
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

function enableButton(email) {
  let button = document.getElementById('submitBtn');
  if (!validateEmail(email.trim())) {
    button.textContent = "Enter Valid Email"
    button.style.borderRightColor = '#FF0000';
    button.style.borderLeftColor = '#FF0000';
    button.style.color = '#FF0000';
    button.style.cursor = 'not-allowed';
    button.disabled = true;
  } else {
    button.textContent = "Submit"
    button.style.borderRightColor = 'unset';
    button.style.borderLeftColor = 'unset';
    button.style.color = 'unset';
    button.style.cursor = 'pointer';
    button.disabled = false;
  }
}

//navbar active
document.addEventListener('DOMContentLoaded', (event) => {
  const sections = document.querySelectorAll('section');
  const navLinks = document.querySelectorAll('#header ul a, #header ul button');

  const options = {
      root: null, 
      rootMargin: '0px',
      threshold: 0.5 
  };

  const callback = (entries, observer) => {
      entries.forEach(entry => {
          navLinks.forEach(link => {
              const targetId = link.onclick.toString().match(/scrollToSection\('(.+?)'\)/)[1];
              if (entry.target.id === targetId) {
                  if (entry.isIntersecting) {
                      link.classList.add('active');
                  } else {
                      link.classList.remove('active');
                  }
              }
          });
      });
  };

  const observer = new IntersectionObserver(callback, options);

  sections.forEach(section => {
      observer.observe(section);
  });
});