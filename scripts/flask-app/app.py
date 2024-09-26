from flask import Flask, render_template
from datetime import datetime
import os
import random

app = Flask(__name__)


@app.route("/")
def index():
    current_datetime = datetime.now()
    return render_template("index.html", time=current_datetime)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))