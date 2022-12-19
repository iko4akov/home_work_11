from utils import load_json_file, candidate_by_skill, candidate_by_name, candidate_by_id
from flask import Flask, render_template

app = Flask(__name__)

json_file = "candidates.json"


@app.route("/")
def index_page():
    """Получает ссылку(json_file) на json фаил, загружает его и переводит в список словарей(people),
     c помощью (load_json_file) для дальнейшей работы, возвращает people в шаблон(list.html)"""
    people = load_json_file(json_file)
    return render_template('list.html', people=people)


@app.route("/candidate/<int:x>")
def candidate_page(x):
    """Получает ссылку(json_file) на .json фаил, загружает его и переводит в список словарей(candidates)
     c помощью (load_json_file) для дальнейшей работы. С помощью функции candidate_by_id, списка словарей
     candidates и переменной x, выводит данные на кандидата по id"""
    candidates = load_json_file(json_file)
    candidate = candidate_by_id(x, candidates)
    return render_template('single.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def search_page(candidate_name):
    """
    1.Загрузка .json файла в список словарей
    2.С начала перевод полученного имя кандитата в нижний регистр, потом перевод всех первых букв в Верхний регистр
    3.С помощью функции candidate_by_name возвращает словарь в ввиде имя(ключ) айди(значение)
    """
    candidates = load_json_file(json_file)
    candidate_lower = candidate_name.lower().title()
    name = candidate_by_name(candidate_lower, candidates)
    return render_template('search.html', name=name)


@app.route("/skill/<skill_name>")
def search_skill_page(skill_name):
    """
    1.Загрузка .json файла в список словарей
    2.С начала перевод полученного скилла в нижний регистр, потом перевод всех первых букв в Верхний регистр
    3.С помощью функции candidate_by_skill возвращает словарь в ввиде: скиллы(ключ) айди(значение)
    :param skill_name: переменная(по факту поисковой запрос)
    :return: рендерит через шаблон и возвращает в виде сколько найдено с сыслками на страницу кандидатов
    """
    candidates = load_json_file(json_file)
    skill = skill_name.lower().title()
    skills = candidate_by_skill(skill, candidates)
    return render_template('skill.html', skills=skills, skill=skill)


if __name__ == '__main__':
    app.run(host="127.0.0.11", port=5001)
