import json


def load_json_file(filename):
    """returns list from .json"""
    with open(filename, encoding="utf-8") as f:
        candidates = json.load(f)
        return candidates


def candidate_by_id(index, candidates):
    """returns data candidate by id"""
    for i in range(len(candidates)):
        if candidates[i]['id'] == index:
            return candidates[i]


def candidate_by_name(name, candidates):
    """:returns data candidate by name"""
    candidates_names = {}
    for i in range(len(candidates)):
        if name in candidates[i]['name']:
            candidates_names[candidates[i]["name"]] = candidates[i]['id']
            return candidates_names


def candidate_by_skill(skill, candidates):
    """:returns data candidate by skill"""
    candidate_skills = {}
    for i in range(len(candidates)):
        if skill in candidates[i]['skills']:
            candidate_skills["skill"] = candidates[i]['id']
            return candidate_skills
