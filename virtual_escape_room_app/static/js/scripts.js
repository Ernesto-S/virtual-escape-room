
    (function($) {
    "use strict"; // Start of use strict
    
        // Get the modal
        var logmodal = document.getElementById("loginModal");
        var regmodal = document.getElementById("registerModal");
        var intmodal = document.getElementById("instructionsModal");
    
        // Get the button that opens the modal
        var login = document.getElementById("login");
        var register = document.getElementById("register");
        var instructions = document.getElementById("instructions");
    
    
        // Get the <span> element that closes the modal
        // When the user clicks on <span> (x), close the modal
        var closeButtons = document.getElementsByClassName("close");
        for (var i = 0; i < closeButtons.length; i++) {
            closeButtons.item(i).onclick = function () {
                logmodal.style.display = "none";
                regmodal.style.display = "none";
                intmodal.style.display = "none";
            }
        }
    
        // When the user clicks on the button, open the modal
        login.onclick = function () {
            logmodal.style.display = "block";
            regmodal.style.display = "none";
            intmodal.style.display = "none";
        }
    
        register.onclick = function () {
            regmodal.style.display = "block";
            logmodal.style.display = "none";
            intmodal.style.display = "none";
        }
    
        instructions.onclick = function () {
            intmodal.style.display = "block";
            logmodal.style.display = "none";
            regmodal.style.display = "none";
        }
    
    
        // When the user clicks anywhere outside of the modal, close it
        window.onclick = function (event) {
            if (event.target == logmodal) {
                logmodal.style.display = "none";
            }
            if (event.target == regmodal) {
                regmodal.style.display = "none";
            }
            if (event.target == intmodal) {
                intmodal.style.display = "none";
            }
        }
        
    // Smooth scrolling using jQuery easing
    $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function() {
      if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
        if (target.length) {
          $('html, body').animate({
            scrollTop: (target.offset().top - 71)
          }, 1000, "easeInOutExpo");
          return false;
        }
      }
    });
  
    // Scroll to top button appear
    $(document).scroll(function() {
      var scrollDistance = $(this).scrollTop();
      if (scrollDistance > 100) {
        $('.scroll-to-top').fadeIn();
      } else {
        $('.scroll-to-top').fadeOut();
      }
    });
  
    // Closes responsive menu when a scroll trigger link is clicked
    $('.js-scroll-trigger').click(function() {
      $('.navbar-collapse').collapse('hide');
    });
  
    // Activate scrollspy to add active class to navbar items on scroll
    $('body').scrollspy({
      target: '#mainNav',
      offset: 80
    });
  
    // Collapse Navbar
    var navbarCollapse = function() {
      if ($("#mainNav").offset().top > 100) {
        $("#mainNav").addClass("navbar-shrink");
      } else {
        $("#mainNav").removeClass("navbar-shrink");
      }
    };
    // Collapse now if page is not at top
    navbarCollapse();
    // Collapse the navbar when page is scrolled
    $(window).scroll(navbarCollapse);
  
  })(jQuery); // End of use strict
  