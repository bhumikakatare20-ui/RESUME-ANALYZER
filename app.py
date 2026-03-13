from flask import Flask, render_template, request
from resume_parser import extract_text
from skills import skills_list

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():

    file = request.files['resume']
    text = extract_text(file)

    if text == "error":
        return "Invalid PDF file"

    detected_skills = []

    for skill in skills_list:
        if skill in text:
            detected_skills.append(skill)

    missing_skills = list(set(skills_list) - set(detected_skills))

    # Skill match percentage
    total_skills = len(skills_list)
    matched = len(detected_skills)

    match_percentage = int((matched / total_skills) * 100)

    # Resume score logic
    resume_score = match_percentage + 20

    if resume_score > 100:
        resume_score = 100

    return render_template(
        'result.html',
        skills=detected_skills,
        missing=missing_skills,
        score=resume_score,
        match=match_percentage
    )


if __name__ == '__main__':
    app.run(debug=True)