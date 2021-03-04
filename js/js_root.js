window.onload = init;

function init() {
    var year = new Date().getFullYear();
    document.getElementById("footer").innerHTML = year + ", RaspiMote.";
    $(".fade").fadeOut(1500);
}

function makeWhite(el) {
    el.style.backgroundColor = "black";
    el.style.filter = "invert(100%)";
}

function makeTransparent(el) {
    el.style.backgroundColor = "#ffffff00";
    el.style.filter = "invert(0)";
}