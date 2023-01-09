import logging
import sys
from flask import Flask, request
from ukrainian_word_stress import Stressifier, StressSymbol

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
app.debug = True
stressify = Stressifier(stress_symbol=StressSymbol.CombiningAcuteAccent)
print("ukr-nlp-api available", file=sys.stderr)


@app.route("/api/stress", methods=["POST"])
def post_stress():
    jsonData = request.get_json()
    # print("before", file=sys.stderr)
    stressedText = {"stressedtext": stressify(jsonData["text"])}
    # print(">", stressedText, file=sys.stderr)
    return stressedText
