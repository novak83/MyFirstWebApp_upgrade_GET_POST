from flask import Flask, render_template, request
import datetime
app = Flask(__name__)

@app.route("/")
def index():
    weather_info = "Danes je zelo lep dan."
    current_year = datetime.datetime.now().year

    cities = ["Ljubljana", "Celje", "Maribor", "Ptuj", "Koper"]
    return render_template("index.html", weather_info=weather_info, current_year=current_year, cities=cities)

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    print(name)
    print(email)
    print(message)

    return render_template("success.html")

@app.route("/portfolio")
def portfolio():
    return render_template("/portfolio.html")

if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)