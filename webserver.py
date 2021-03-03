from flask import Flask, request, send_file, send_from_directory, redirect
from cheroot.wsgi import Server as WSGIServer, PathInfoDispatcher as WSGIPathInfoDispatcher
from cheroot.ssl.builtin import BuiltinSSLAdapter

app = Flask(__name__)

@app.route('/')
def index():
    if "docs.raspimote.tk" in request.url_root:
        return send_file("index.html")
    elif "www.raspimote.tk" in request.url_root:
        return redirect(request.url.replace("www.raspimote.tk", "raspimote.tk")), 301
    elif "raspimote.tk" in request.url_root:
        return send_file("root_website.html")
    else:
        return "<h1>Nothing here, for the moment...</h1>", 404

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