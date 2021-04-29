from flask import Flask, redirect, url_for, render_template, request
from cs50 import SQL

app = Flask('app')

db = SQL("sqlite:///babysitters.db")
rows = db.execute("SELECT * FROM babysitters")

@app.route('/')
def blank():
	return redirect(url_for("home"))

@app.route("/home", methods=["POST", "GET"])
def home():
	return render_template("home.html");

@app.route("/explore")
def explore():
	return render_template("explore.html", rows=rows)

@app.route("/signup", methods=["POST", "GET"])
def signup():
	if request.method == "POST":
		if(request.form.get("name") == "" or request.form.get("age") == "" or request.form.get("minSal") == "" or request.form.get("email") == ""):
			return render_template("signup.html")
		db.execute("INSERT INTO babysitters (name, age, minSal, email, phoneNumber) VALUES ('" + request.form.get('name') + "', " + request.form.get('age') + ", " + request.form.get('minSal') + ", '" + request.form.get('email') + "', " + request.form.get('phone') + ")")
		return redirect(url_for("home"))
	else:
		return render_template("signup.html")

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080)