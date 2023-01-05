import logging
from flask import Flask, jsonify, request, Response, g

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
app.debug = True

@app.route("/api/stress", methods=["POST"])
def post_stress():

    jsonData = request.get_json()

    stressedText = {"stressedtext": jsonData["text"].lower()}

    return stressedText

@app.route("/")
def get_root():
    return "<body><p>Hello World!</p></body>"
