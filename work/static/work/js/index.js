// Add slide toggle to filter controls on click
// Adapted from https://stackoverflow.com/questions/33956637/javascript-native-implementation-div-display-hide-with-animate
window.onload = () => {
    let toggle = document.getElementById('toggle-filter');
    let controls = document.getElementById('control-options');

    toggle.addEventListener('click', (e) => {
        let flag = controls.classList.contains('show');

        if (flag) {
            controls.classList.remove('show');
        } else {
            controls.classList.add('show');
        }
    });
};