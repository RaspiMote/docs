function year() {
    var year = new Date().getFullYear();
    document.getElementById("footer").innerHTML = year + ", RaspiMote.";
}