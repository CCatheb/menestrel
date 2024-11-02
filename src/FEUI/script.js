// Alterner entre deux images - On/Off
document.addEventListener("DOMContentLoaded", function() {
    var image = document.getElementById("on-off");
    var statusText = document.getElementById("statusText-onOff");
    var firstImageSrc = "img/off.png";
    var secondImageSrc = "img/on.png";
    var currentImage = firstImageSrc;
  
    image.addEventListener("click", function() {
        // Alterner entre les deux sources d'image
        if (currentImage === firstImageSrc) {
            currentImage = secondImageSrc;
            statusText.textContent = 'Off';
        } else {
            currentImage = firstImageSrc;
            statusText.textContent = 'On';
        }
        // Modifier la source de l'image
        image.src = currentImage;
    });
});

// Alterner entre deux images - Login/Logout
document.addEventListener("DOMContentLoaded", function() {
    var image = document.getElementById("login-logout");
    var statusText = document.getElementById("statusText-loginLogout");
    var firstImageSrc = "img/login.png";
    var secondImageSrc = "img/logout.png";
    var currentImage = firstImageSrc;
  
    image.addEventListener("click", function() {
        // Alterner entre les deux sources d'image
        if (currentImage === firstImageSrc) {
            currentImage = secondImageSrc;
            statusText.textContent = 'Login';
        } else {
            currentImage = firstImageSrc;
            statusText.textContent = 'Logout';
        }
        // Modifier la source de l'image
        image.src = currentImage;
    });
});

// Alterner entre deux images - Day/Night
document.addEventListener("DOMContentLoaded", function() {
    var image = document.getElementById("day-night");
    var firstImageSrc = "img/soleil.png";
    var secondImageSrc = "img/lune.png";
    var currentImage = firstImageSrc;
  
    image.addEventListener("click", function() {
        // Alterner entre les deux sources d'image
        if (currentImage === firstImageSrc) {
            currentImage = secondImageSrc;
        } else {
            currentImage = firstImageSrc;
        }
        // Modifier la source de l'image
        image.src = currentImage;
    });
});

// Ecouter boutons de la section Scene
document.addEventListener("DOMContentLoaded", function() {
    var buttons = document.querySelectorAll(".scene-btn");
  
    buttons.forEach(function(button) {

        button.addEventListener("click", function() {

            if (!button.classList.contains("active")) {
                // Désactiver la classe active pour tous les boutons
                buttons.forEach(function(btn) {
                btn.classList.remove("active");
                });
                // Activer la classe active pour le bouton cliqué
                button.classList.add("active");
            } else {
                // Retirer la classe active si elle est déjà présente
                button.classList.remove("active");
            }
            make_request("scene", button.textContent);
        });

    });

});

// Ecouter bouton de la section Ambiance - Phase
document.addEventListener("DOMContentLoaded", function() {
    var buttons = document.querySelectorAll(".phase-btn");
    var reset = document.getElementById("reset-phase");
  
    buttons.forEach(function(button) {

        button.addEventListener("click", function() {

            if (!button.classList.contains("active")) {
                // Désactiver la classe active pour tous les boutons
                buttons.forEach(function(btn) {
                btn.classList.remove("active");
                });
                // Activer la classe active pour le bouton cliqué
                button.classList.add("active");
            } else {
                // Retirer la classe active si elle est déjà présente
                button.classList.remove("active");
            }
            make_request("phase", button.textContent);
        });

    });

    reset.addEventListener("click", function() {

        // Désactiver la classe active pour tous les boutons
        buttons.forEach(function(btn) {
            btn.classList.remove("active");
        });

    });

});

// Ecouter bouton de la section Ambiance - Meteo
document.addEventListener("DOMContentLoaded", function() {
    var buttons = document.querySelectorAll(".meteo-btn");
    var reset = document.getElementById("reset-meteo");
  
    buttons.forEach(function(button) {

        button.addEventListener("click", function() {

            if (!button.classList.contains("active")) {
                // Désactiver la classe active pour tous les boutons
                buttons.forEach(function(btn) {
                btn.classList.remove("active");
                });
                // Activer la classe active pour le bouton cliqué
                button.classList.add("active");
            } else {
                // Retirer la classe active si elle est déjà présente
                button.classList.remove("active");
            }
            make_request("meteo", button.textContent);
        });

    });

    reset.addEventListener("click", function() {

        // Désactiver la classe active pour tous les boutons
        buttons.forEach(function(btn) {
            btn.classList.remove("active");
        });

    });

});

// Ecouter bouton de la section Ambiance - Ambiance
document.addEventListener("DOMContentLoaded", function() {
    var buttons = document.querySelectorAll(".ambiance-btn");
  
    buttons.forEach(function(button) {

        button.addEventListener("click", function() {
            button.classList.toggle("active");
            make_request("ambiance", button.textContent);
        });
        
    });

});
  
function make_request(group, value) {

    url = "http://192.168.0.33:8000/" + group

    fetch(url, {
        method: "POST",
        headers: {
            "Content-type": "application/json; charset=UTF-8"
          },
        "body": JSON.stringify({
            "value": value
        })
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
}