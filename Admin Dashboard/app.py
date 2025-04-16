from flask import Flask, render_template, request
from data import headsets

# Initialize Flask app
app = Flask(__name__)

# Route: Calendar and Table Views
@app.route("/")
def dashboard():
    view = request.args.get("view", "table")
    if view == "calendar":
        return render_template("calendar.html", headsets=headsets)
    return render_template("table.html", headsets=headsets)

if __name__ == "__main__":
    app.run(debug=True)