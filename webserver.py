from flask import Flask, request, send_file, send_from_directory, redirect
from cheroot.wsgi import Server as WSGIServer, PathInfoDispatcher as WSGIPathInfoDispatcher
from cheroot.ssl.builtin import BuiltinSSLAdapter

app = Flask(__name__)

mobile_user_agents = ["opera mini", "android", "fennec", "mobile", "iphone", "symbian", "blackberry", "nexus", "nokia"]

@app.errorhandler(404)
def page_not_found(e):
    return send_file('404.html'), 404

@app.route('/')
def index():
    if "docs.raspimote.tk" in request.url_root:
        return send_file("index.html")
    elif "www.raspimote.tk" in request.url_root:
        return redirect(request.url.replace("www.raspimote.tk", "raspimote.tk")), 301
    elif "raspimote.tk" in request.url_root:
        if any(ext in request.headers.get('User-Agent').lower() for ext in mobile_user_agents):
            return send_file("root_website_mob.html")
        else:
            return send_file("root_website.html")
    else:
        return "<h1>Nothing here, for the moment...</h1>", 404

@app.route('/mailto')
def mailto():
    if (not "docs.raspimote.tk" in request.url_root) and ("raspimote.tk" in request.url_root):
        return redirect("mailto:hello@raspimote.tk")

@app.route('/css/<path:path>')
def css(path):
    if "raspimote.tk" in request.url_root:
        return send_from_directory('css', path)
    else:
        return "<h1>Nothing here, for the moment...</h1>", 404

@app.route('/img/<path:path>')
def img(path):
    if "raspimote.tk" in request.url_root:
        return send_from_directory('img', path)
    else:
        return "<h1>Nothing here, for the moment...</h1>", 404

@app.route('/fonts/<path:path>')
def fonts(path):
    if "raspimote.tk" in request.url_root:
        return send_from_directory('fonts', path)
    else:
        return "<h1>Nothing here, for the moment...</h1>", 404

@app.route('/js/<path:path>')
def js(path):
    if "raspimote.tk" in request.url_root:
        return send_from_directory('js', path)
    else:
        return "<h1>Nothing here, for the moment...</h1>", 404




my_app = WSGIPathInfoDispatcher({'/': app})
server = WSGIServer(('0.0.0.0', 4430), my_app)

ssl_cert = "cert.pem"
ssl_key = "key.key"
server.ssl_adapter =  BuiltinSSLAdapter(ssl_cert, ssl_key, None)

if __name__ == '__main__':
   try:
      server.start()
   except KeyboardInterrupt:
      server.stop()