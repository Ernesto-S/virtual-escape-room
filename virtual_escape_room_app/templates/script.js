$(document).ready(function() {

    // Get the modal
    var logmodal = document.getElementById("loginModal");
    var regmodal = document.getElementById("registerModal");
    var intmodal = document.getElementById("instructionsModal");


    // Get the button that opens the modal
    var login = document.getElementById("login");
    var register = document.getElementById("register");
    var instructions = document.getElementById("instructions");


    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks on the button, open the modal
    login.onclick = function() {
    logmodal.style.display = "block";
    }

    register.onclick = function() {
    regmodal.style.display = "block";
    }

    instructions.onclick = function() {
    intmodal.style.display = "block";
    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
    logmodal.style.display = "none";
    regmodal.style.display = "none";
    intmodal.style.display = "none";
    }
    
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
    }
});

