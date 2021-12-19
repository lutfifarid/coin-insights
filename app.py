from flask import Flask, Response, url_for
import waitress 
import gunicorn 
import os

app = Flask(__name__)
# app.run(debug=True)

@app.route('/')
def index():
  return '<h1>Coin Insight Comming Soon</h1>'

if __name__ == "__main__":
     app.debug = False
     port = int(os.environ.get('PORT', 3355))
     waitress.serve(app, port=port)