from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def hello():
    tz = pytz.timezone("Europe/Berlin")
    now = datetime.now(tz)
    serverzeit = now.strftime("%d.%m.%Y · %H:%M:%S Uhr")
    return render_template("index.html", serverzeit=serverzeit)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
