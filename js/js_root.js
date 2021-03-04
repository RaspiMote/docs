window.onload = init;
// $('*').on('click', function(){ return true; });
// navigator.appVersion.toLowerCase().includes("iphone")

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}  

function init() {
    var year = new Date().getFullYear();
    document.getElementById("footer").innerHTML = year + ", RaspiMote.";
    let url = 'https://api.github.com/repos/RaspiMote/RaspiMote/releases';
    fetch(url).then(res => res.json()).then((out) => {
        if (out[0] != undefined) {
            var version = out[0]["tag_name"];
            var release_url = out[0]["html_url"];
            document.getElementById("version").innerHTML = "The current version of RaspiMote is " + version + ". Download it <a target=\"_blank\" href=\"" + release_url + "\">here</a>."
        }
        else {
            document.getElementById("version").innerHTML = "This project is currently in development. Consequently, no release is available for the moment."
        }
    })
    .catch(err => {
        throw err
    });
    $(".fade").fadeOut(1500);
}

function makeWhite(el) {
    if (navigator.appVersion.toLowerCase().includes("iphone") == false) {
        el.style.backgroundColor = "black";
        el.style.filter = "invert(100%)";
    }
}

function makeTransparent(el) {
    if (navigator.appVersion.toLowerCase().includes("iphone") == false) {
        el.style.backgroundColor = "#ffffff00";
        el.style.filter = "invert(0)";
    }
}

function selectButtonWKi(el) {
    if (navigator.appVersion.toLowerCase().includes("iphone")) {
        el.style.backgroundColor = "black";
        el.style.filter = "invert(100%)";
        await sleep(1000);
        el.style.backgroundColor = "#ffffff00";
        el.style.filter = "invert(0)";
    }
}