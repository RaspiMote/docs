window.onload = init;

function init() {
    var year = new Date().getFullYear();
    document.getElementById("footer").innerHTML = year + ", RaspiMote.";
    $(".fade").fadeOut(1500);
}

function toDocs() {
    var url = "https://docs.raspimote.tk/";
    if (KeyPressing.isKeyPressed(17) || KeyPressing.isKeyPressed(16)) {
        window.open(url);
    }
    else {
        window.location.href = url;
    }
}

function toGitHub() {
    var url = "https://github.com/RaspiMote/RaspiMote";
    if (KeyPressing.isKeyPressed(17) || KeyPressing.isKeyPressed(16)) {
        window.open(url);
    }
    else {
        window.location.href = url;
    }
}

function makeWhite(el) {
    el.style.backgroundColor = "black";
    el.style.filter = "invert(100%)";
}

function makeTransparent(el) {
    el.style.backgroundColor = "#ffffff00";
    el.style.filter = "invert(0)";
}