document.addEventListener("DOMContentLoaded", function() {
        var passwordField = document.getElementById("password");
        var toggleIcon = document.querySelector(".toggle-password");

        // Show password while holding the mouse down
        toggleIcon.addEventListener("mousedown", function() {
            passwordField.type = "text";
        });

        // Hide password when releasing the mouse
        toggleIcon.addEventListener("mouseup", function() {
            passwordField.type = "password";
        });

        // Also hide if the mouse leaves the icon (for better usability)
        toggleIcon.addEventListener("mouseleave", function() {
            passwordField.type = "password";
        });
    });

    document.addEventListener("DOMContentLoaded", function() {
        setTimeout(function() {
            let alertBox = document.querySelector(".alert");
            if (alertBox) {
                alertBox.classList.add("fade-out");
                setTimeout(() => alertBox.remove(), 1000); // Removes from DOM
            }
        }, 3000); // 3 seconds delay before fade
    });


const passwordField = document.getElementById("password");
const capsWarning = document.getElementById("caps-warning");

passwordField.addEventListener("keyup", function(event) {
    if (event.getModifierState("CapsLock")) {
        capsWarning.style.display = "block";
    } else {
        capsWarning.style.display = "none";
    }
});


document.addEventListener("DOMContentLoaded", function() {
        const loginForm = document.querySelector("form");
        const loaderOverlay = document.getElementById("loaderOverlay");

        // Hide loader when page loads
        loaderOverlay.style.display = "none";

        loginForm.addEventListener("submit", function(event) {
            loaderOverlay.style.display = "flex"; // Show loader
        });
    });