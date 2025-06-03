from flask import render_template
from app import app
from os import listdir

@app.route('/testes')
def teste():
    artesStorie = listdir('app/static/images/Artes/Storie/')
    artesFeed = listdir('app/static/images/Artes/Feed/')
    return render_template('teste.html', artesStorie=artesStorie, artesFeed=artesFeed)