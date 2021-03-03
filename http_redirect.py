from flask import Flask, request, redirect
from waitress import serve

app = Flask(__name__)

@app.errorhandler(404)
def https(e):
    return redirect(request.url.replace("http://", "https://")), 301




if __name__ == "__main__":
    serve(app, port=8000, host="0.0.0.0")