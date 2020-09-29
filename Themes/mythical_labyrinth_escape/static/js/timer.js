function countdown(element, minutes) {
    // Fetch the display element
    var el = document.getElementById(element);
    var seconds = 0;
    // Set the timer
    var interval = setInterval(function() {
        if(seconds == 0) {
            if(minutes == 0) {
                (el.innerHTML = "STOP!");     

                clearInterval(interval);
                return;
            } else {
                minutes--;
                seconds = 59;
            }
        }
        
        el.innerHTML = minutes;
        seconds--;
    }, 1000);
}
countdown('timer', 10)