from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify({"data": "Hello world!!"})
@app.route("/backend")
def hello_world():
    return jsonify({"data": "Hello backend!!"})
