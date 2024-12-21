import json

from flask import Flask, render_template

app = Flask(__name__)

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def home():
    template = 'home.html'
    projects = load_json('data/projects.json')
    news = load_json('data/news.json')
    skills = load_json('data/skills.json')
    return render_template(
        template,
        projects=projects, 
        news=news, 
        skills=skills
    )

if __name__ == '__main__':
    app.run(debug=False, port=8088)