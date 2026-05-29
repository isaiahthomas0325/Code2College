# StudyPal AI

## Description

StudyPal AI is a Flask-based web application that helps students turn their notes into study questions. Users can paste notes into a text box and generate review questions to help reinforce learning.

This project was built using Python, Flask, HTML, and GitHub while practicing AI-assisted software engineering.

## Features

- Enter study notes through a web interface
- Generate review questions from notes
- Input validation for empty or insufficient input
- Error handling for invalid submissions
- Modular code structure using multiple files
- Automated test cases for question generation

## Technologies Used

- Python
- Flask
- HTML
- Git
- GitHub

## Installation

1. Clone the repository:

git clone https://github.com/isaiahthomas0325/Code2College.git

2. Navigate to the project folder:

cd Code2College

3. Create and activate a virtual environment:

python3 -m venv .venv

source .venv/bin/activate

4. Install dependencies:

pip install -r requirements.txt

## Running the Application

Start the Flask application:

python3 app.py

Open your browser and visit:

http://127.0.0.1:5000

## Example Usage

Input:

Photosynthesis uses sunlight. Plants need water.

Output:

- What is meant by: Photosynthesis uses sunlight?
- What is meant by: Plants need water?

## Project Structure

- app.py - Flask application
- question_generator.py - Question generation logic
- test_question_generator.py - Test cases
- templates/ - HTML templates
- static/ - CSS and JavaScript files

## Future Improvements

- AI-generated questions using a language model
- Flashcard generation
- Multiple question types
- User accounts and saved study sets