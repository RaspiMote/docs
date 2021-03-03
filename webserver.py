from flask import Flask, request, send_file, send_from_directory
from cheroot.wsgi import Server as WSGIServer, PathInfoDispatcher as WSGIPathInfoDispatcher
from cheroot.ssl.builtin import BuiltinSSLAdapter

app = Flask(__name__)

@app.route('/')
def index():
    if request.url_root == "https://docs.raspimote.tk":
        return send_file("index.html")
    else:
        return "<h1>Nothing here</h1>", 404

@app.route('/css/<path:path>')
def css(path):
    if request.url_root == "https://docs.raspimote.tk":
        return send_from_directory('css', path)

@app.route('/img/<path:path>')
def img(path):
    if request.url_root == "https://docs.raspimote.tk":
        return send_from_directory('img', path)

@app.route('/js/<path:path>')
def js(path):
    if request.url_root == "https://docs.raspimote.tk":
        return send_from_directory('js', path)




my_app = WSGIPathInfoDispatcher({'/': app})
server = WSGIServer(('0.0.0.0', 9876), my_app)

ssl_cert = "cert.pem"
ssl_key = "key.key"
server.ssl_adapter =  BuiltinSSLAdapter(ssl_cert, ssl_key, None)

if __name__ == '__main__':
   try:
      server.start()
   except KeyboardInterrupt:
      server.stop()