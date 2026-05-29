from flask import Flask, render_template, request

app = Flask(__name__)

def generate_questions(notes):

    """
    Converts notes into simple study questions.

    Preconditions:
        notes is a string.

    Postconditions:
        Returns a list of generated questions.
    """

    questions = []

    if not notes.strip():
        return questions

    sentences = notes.split(".")

    for sentence in sentences:

        sentence = sentence.strip()

        if sentence:
            questions.append(
                f"What is meant by: {sentence}?"
            )

    return questions


@app.route("/", methods=["GET", "POST"])
def home():

    questions = []
    error = ""

    if request.method == "POST":

        notes = request.form.get("notes", "").strip()

        if len(notes) == 0:

            error = "Please enter some notes."

        elif len(notes) < 10:

            error = "Please enter more detailed notes."

        else:

            questions = generate_questions(notes)

    return render_template(
        "index.html",
        questions=questions,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)