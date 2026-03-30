from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate_pass():
    name = request.form.get("name")
    route = request.form.get("route")
    date = request.form.get("date")

    return render_template("pass.html", name=name, route=route, date=date)


if __name__ == "__main__":
    app.run(debug=True)
