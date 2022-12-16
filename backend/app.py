from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify({"data": "Hello world!!"})
@app.route("/haha")
def hello_world():
    return jsonify({"data": "Hello haha!!"})
