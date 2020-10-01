function countdown(element, minutes, seconds) {
    // Fetch the display element
    var el = document.getElementById(element);

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

        if(minutes > 0) {
            var minute_text = minutes + ':';
        } else {
            var minute_text = '';
        }
        
        el.innerHTML = minute_text + seconds;
        seconds--;
    }, 1000);
}
countdown('timer', 10, 0)