document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("generate_number_button").addEventListener("click", function() {
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "/number", true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                var randomNumberDisplay = document.getElementById("random_number_display");
                randomNumberDisplay.textContent = "Random Number: " + xhr.responseText;
            }
        };
        xhr.send();
    });

    document.getElementById("log_toto_button").addEventListener("click", function() {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/log_toto", true);
        xhr.send();
    });

    document.getElementById("start_bot").addEventListener("click", function() {
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "/start", true);
        xhr.send();
    })

    document.getElementById("stop_bot").addEventListener("click", function() {
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "/stop", true);
        xhr.send();
    })
    document.getElementById("join_voice").addEventListener("click", function() {
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "/join-voice", true);
        xhr.send();
    })
});
