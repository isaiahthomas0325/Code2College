from flask import Flask, render_template, request

app = Flask(__name__)

def generate_questions(notes):

    questions = []

    lines = notes.split(".")

    for line in lines:

        line = line.strip()

        if line != "":
            question = f"What is meant by: {line}?"
            questions.append(question)

    return questions


@app.route("/", methods=["GET", "POST"])
def home():

    questions = []

    if request.method == "POST":

        notes = request.form.get("notes")

        if notes.strip() != "":
            questions = generate_questions(notes)

    return render_template("index.html", questions=questions)


if __name__ == "__main__":
    app.run(debug=True)