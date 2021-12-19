from flask import Flask, Response, url_for
from waitress import serve
import os

app = Flask(__name__)
# app.run(debug=True)

@app.route('/')
def index():
  return '<h1>I want to Deploy Flask</h1>'

if __name__ == "__main__":
     app.debug = False
     port = int(os.environ.get('PORT', 33507))
     serve(app, port=port)