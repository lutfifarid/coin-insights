from flask import Flask, Response, url_for
from waitress import serve

app = Flask(__name__)
# app.run(debug=True)

@app.route('/')
def index():
  return '<h1>I want to Deploy Flask</h1>'

serve(app, listen='*:8080')