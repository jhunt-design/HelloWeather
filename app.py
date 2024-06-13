from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")


