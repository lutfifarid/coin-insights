from flask import Flask, Response, url_for
import waitress 
import gunicorn 
import os

app = Flask(__name__)
# app.run(debug=True)

@app.route('/')
def index():
  return '<h1>I want to Deploy Flask</h1>'

if __name__ == "__main__":
     app.debug = False
     port = int(os.environ.get('PORT', 33507))
     waitress.serve(app, port=port)