var r = document.querySelector(':root');
var dark = document.getElementById("dark");
var light = document.getElementById("light");

var description = document.getElementById("description");
var information = document.getElementById("information");
var review = document.getElementById("review");

var black_big = document.getElementById("watch_black_big");
var black = document.getElementById("watch_black");
var blue = document.getElementById("watch_blue");
var pink = document.getElementById("watch_pink");
theme_mode = 'light'

function set_theme() {
    if (theme_mode == 'light'){
        light.style.display = "block";
        dark.style.display = "none";
        r.style.setProperty('--bg-color', '#1f242d');
        r.style.setProperty('--second-bg-color', '#323946');
        r.style.setProperty('--text-color', '#fff');
        black_big.src = "./img/watch_black2.jpg";
        pink.style.backgroundImage = "url(./img/watch_pink2.jpg)";
        blue.style.backgroundImage = "url(./img/watch_blue2.jpg)";
        black.style.backgroundImage = "url(./img/watch_black2.jpg)";
        theme_mode = 'dark'
    }
    else{
        light.style.display = "none";
        dark.style.display = "block";
        r.style.setProperty('--bg-color', 'whitesmoke');
        r.style.setProperty('--second-bg-color', 'rgb(220, 220, 220)');
        r.style.setProperty('--text-color', 'black');
        black_big.src = "./img/watch_black.jpg";
        pink.style.backgroundImage = "url(./img/watch_pink.jpg)";
        blue.style.backgroundImage = "url(./img/watch_blue.jpg)";
        black.style.backgroundImage = "url(./img/watch_black.jpg)";
        theme_mode = 'light'
    }
}
function set_description() {
    description.style.display = "block";
    information.style.display = "none";
    review.style.display = "none";
}
function set_information() {
    information.style.display = "block";
    description.style.display = "none";
    review.style.display = "none";
}
function set_review() {
    review.style.display = "block";
    information.style.display = "none";
    description.style.display = "none";
}