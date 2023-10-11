theme_mode = 'dark'
setting_mode = 'close'
var r = document.querySelector(':root');
var sun = document.getElementById("sun");
var moon = document.getElementById("moon");
var color_box = document.getElementById('color');
function set_green() {
    r.style.setProperty('--main-color', 'rgb(2, 156, 72)');
}
function set_blue() {
    r.style.setProperty('--main-color', 'rgb(0, 195, 255)');
}
function set_red() {
    r.style.setProperty('--main-color', 'rgb(245, 8, 0)');
}
function set_orange() {
    r.style.setProperty('--main-color', 'rgb(253, 119, 9)');
}
function set_purple() {
    r.style.setProperty('--main-color', '#754ff7');
}

function setting_close() {
    if (setting_mode == 'open'){
        color_box.style.right = '-26rem';
        setting_mode = 'close'
    }
    else{
        color_box.style.right = '1rem';
        setting_mode = 'open'
    }
}

function set_theme() {
    if (theme_mode == 'light'){
        sun.style.display = "block";
        moon.style.display = "none";
        r.style.setProperty('--bg-color', '#1f242d');
        r.style.setProperty('--second-bg-color', '#323946');
        r.style.setProperty('--text-color', '#fff');
        theme_mode = 'dark'
    }
    else{
        sun.style.display = "none";
        moon.style.display = "block";
        r.style.setProperty('--bg-color', 'whitesmoke');
        r.style.setProperty('--second-bg-color', 'rgb(220, 220, 220)');
        r.style.setProperty('--text-color', 'black');
        theme_mode = 'light'
    }
}