from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == "__main__":
  os.environ['PORT']
  app.run(debug=False, host='0.0.0.0', port=80)