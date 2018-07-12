import os
from flask import Flask, render_template
application = app = Flask(__name__)

@app.route("/")
def home():
#    return "Hello World!"
    return render_template("home.html")
@app.route("/about/")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    # BIND to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
