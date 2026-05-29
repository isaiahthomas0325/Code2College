# AI Collaboration Log

## Tools Used

- ChatGPT

## Prompt Examples

### Prompt 1: Setting Up Flask

What I asked:

How do I create a Flask project structure for my capstone project?

What worked:

The response provided a clear folder structure and explained the purpose of each file.

What I changed:

I customized the project into a StudyPal AI application focused on generating study questions.

---

### Prompt 2: Git and GitHub Help

What I asked:

How do I initialize Git, create commits, and push my project to GitHub?

What worked:

The response explained Git commands step-by-step and helped me understand commits and pushes.

What I changed:

I used the commands and adjusted my workflow based on my project structure.

---

### Prompt 3: Debugging Import Errors

What I asked:

Why am I getting an ImportError when importing generate_questions?

What worked:

The response helped identify that my question_generator.py file was empty.

What I changed:

I added the missing function and tested the application again.

## Bugs Found in AI Code

1. ImportError after refactoring because the question generation function was not properly placed in question_generator.py. I fixed this by moving the function into the correct file and saving it.

2. Error messages were not displaying correctly because the template logic was inside the question loop. I moved the error display outside the loop.

3. Indentation issues occurred while adding input validation to app.py. I corrected the indentation and retested the application.

## Key Learnings

- Small, specific prompts produce better AI responses.
- AI-generated code should always be tested before being trusted.
- Refactoring improves code organization and readability.
- Git commits should be made frequently with meaningful messages.
- Verification is just as important as generation when using AI tools.

## Reflection

At the start of this project, I mainly used AI to help me with basic things to tag along with the basic code I started with. By the end of the project, I used AI as a collaborator for planning, debugging, testing, and improving code quality while still verifying all results myself.