function changeColor() {
    // Get all "nav-link" elements
    var navLinks = document.getElementsByClassName("nav-link");

    // Add event listener to each "nav-link"
    for (var i = 0; i < navLinks.length; i++) {
        navLinks[i].addEventListener("click", function () {
            // Remove "active" class from all "nav-link" elements
            for (var j = 0; j < navLinks.length; j++) {
                navLinks[j].classList.remove("active");
            }

            // Add "active" class to clicked "nav-link" element
            this.classList.add("active");
        });
    }
}

document.addEventListener("DOMContentLoaded", changeColor);
