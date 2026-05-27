from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    notes = ""

    if request.method == "POST":
        notes = request.form.get("notes")

    return render_template("index.html", notes=notes)

if __name__ == "__main__":
    app.run(debug=True)