var r = document.querySelector(':root');
var dark = document.getElementById("dark");
var light = document.getElementById("light");
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

        black.src = "./img/watch_black2.jpg";
        blue.src = "./img/watch_blue2.jpg"
        pink.src = "./img/watch_pink2.jpg"
        theme_mode = 'dark'
    }
    else{
        light.style.display = "none";
        dark.style.display = "block";
        r.style.setProperty('--bg-color', 'whitesmoke');
        r.style.setProperty('--second-bg-color', 'rgb(220, 220, 220)');
        r.style.setProperty('--text-color', 'black');

        black.src = "./img/watch_black.jpg";
        blue.src = "./img/watch_blue.jpg"
        pink.src = "./img/watch_pink.jpg"
        theme_mode = 'light'
    }
}