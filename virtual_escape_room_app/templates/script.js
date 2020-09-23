$(document).ready(function () {

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
});

