window.onload = init;

function init() {
    var year = new Date().getFullYear();
    document.getElementById("footer").innerHTML = year + ", RaspiMote.";
    $(".fade").fadeOut(1500);
}

function windowLocation(url){
    var X = setTimeout(function(){
        window.location.replace(url);
        return true;
    },300);

    if( window.location = url ){
        clearTimeout(X);
        return true;
    } else {
        if( window.location.href = url ){
            clearTimeout(X);
            return true;
        }else{
            clearTimeout(X);
            window.location.replace(url);
            return true;
        }
    }
    return false;
};

function toDocs() {
    var url = "https://docs.raspimote.tk/";
    if (KeyPressing.isKeyPressed(17) || KeyPressing.isKeyPressed(16)) {
        window.open(url);
    }
    else {
        windowLocation(url);
    }
}

function toGitHub() {
    var url = "https://github.com/RaspiMote/RaspiMote";
    if (KeyPressing.isKeyPressed(17) || KeyPressing.isKeyPressed(16)) {
        window.open(url);
    }
    else {
        windowLocation(url);
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