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