from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('index.html')

app.run(host='0.0.0.0', port=5050, debug=True)