from flask import Flask, render_template
from quote import hent_quote

app = Flask(__name__)

quotes_list = hent_quote()


@app.route("/")
def index():
    navn = "Sandvika"
    return render_template("index.html", navn=navn)

@app.route("/vaer")
def vaer():
    return render_template("vaer.html")

@app.route("/quote")
def quote():
    return render_template("quote.html", quotes_list = quotes_list)


@app.route("/time")
def time():
    return render_template("time.html")



app.run(debug=True)
