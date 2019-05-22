// Move nav options to cneter if screen is small
window.addEventListener('resize', () => {
    let width = window.innerWidth;

    let nav_options = document.getElementById('nav-options');
    
    // Where logo overflow starts
    if (width <= 670) {
        // Move options from right to middle
        nav_options.classList.remove('uk-navbar-right');
        nav_options.classList.remove('uk-margin-large-right');
        nav_options.classList.add('uk-navbar-center');
    } else {
        nav_options.classList.remove('uk-navbar-center');
        nav_options.classList.add('uk-margin-large-right');
        nav_options.classList.add('uk-navbar-right');
    }
});