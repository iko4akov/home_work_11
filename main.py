from utils import load_json_file, candidate_by_skill, candidate_by_name, candidate_by_id
from flask import Flask, render_template

app = Flask(__name__)

jsonfile = "candidates.json"

candidates = load_json_file(jsonfile)


@app.route("/")
def index_page():
    people = candidates
    return render_template('list.html', people=people)


@app.route("/candidate/<int:x>")
def candidate_page(x):
    candidate = candidate_by_id(x, candidates)
    return render_template('single.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def search_page(candidate_name):
    candidate_lower = candidate_name.lower().title()
    name = candidate_by_name(candidate_lower, candidates)
    count = len(name)
    return render_template('search.html', name=name, count=count)


@app.route("/skill/<skill_name>")
def search_skill_page(skill_name):
    skill = skill_name.lower().title()
    skills = candidate_by_skill(skill, candidates)
    count = len(skills)
    return render_template('skill.html', skills=skills, count=count, skill=skill)


if __name__ == '__main__':
    app.run(host="127.0.0.11", port=5001)
