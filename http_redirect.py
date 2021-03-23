from flask import Flask, request, redirect, send_file
from waitress import serve

app = Flask(__name__)

old_user_agents = ["msie", "internet explorer", "netscape", "trident", "navigator/"]

@app.errorhandler(404)
def https(e):
    return redirect(request.url.replace("http://", "https://")), 301

@app.route("/")
def website():
    if "old.raspimote.tk" in request.url_root:
        return send_file("old_website.html")
    elif any(ext in request.headers.get('User-Agent').lower() for ext in old_user_agents) and ("/raspimote.tk" or "www.raspimote.tk") in request.url_root:
        return redirect("http://old.raspimote.tk/"), 301
    else:
        return redirect(request.url.replace("http://", "https://")), 301

@app.route("/docs")
def docs():
    if "old.raspimote.tk" in request.url_root:
        return "No simplified version for old browsers is disponible now. Full version at <a href=\"https://docs.raspimote.tk/\">https://docs.raspimote.tk/</a>."
    else:
        return redirect(request.url.replace("http://", "https://")), 301

@app.route("/old_website.css")
def css():
    if "old.raspimote.tk" in request.url_root:
        return send_file("css/old_website.css")
    else:
        return redirect(request.url.replace("http://", "https://")), 301

@app.route("/RaspiMote_logo.ico")
def ico():
    if "old.raspimote.tk" in request.url_root:
        return send_file("img/RaspiMote_logo.ico")
    else:
        return redirect(request.url.replace("http://", "https://")), 301

@app.route("/RaspiMote_logo_500px.png")
def png():
    if "old.raspimote.tk" in request.url_root:
        return send_file("img/RaspiMote_logo_500px.png")
    else:
        return redirect(request.url.replace("http://", "https://")), 301

if __name__ == "__main__":
    serve(app, port=8000, host="0.0.0.0")