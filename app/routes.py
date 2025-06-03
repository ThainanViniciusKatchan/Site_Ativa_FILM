import os
from datetime import date
from app import app
from flask import render_template
from os import listdir


# Rota para página principal do site
@app.route('/')


@app.route('/principal')
def principal():
    # Variável para receber os arquivos da pasta "LogoClientes" e enviar para o arquivo HTML
    LogoClientes = listdir('app/static/images/LogoClientes')
    # Variável que recebe os dados de data e envia para o arquivo HTML assim a data atual
    # mudara automaricamente no roda pé
    ano = date.today().year
    return render_template('base.html', ano=ano, LogoClientes=LogoClientes)


# Função para retornar caso a url inserida não exista
@app.errorhandler(404)
def pagina_inexistente(error):
    return render_template('base.html')


# Rota para página de artes do site
@app.route('/galeriaArtes')
def galeriaArtes():
    # Variáveis que recebem as artes de Storie e Feed e enviam os aquivos da pasta para p html
    artesStorie = listdir('app/static/images/Artes/Storie/')
    artesFeed = listdir('app/static/images/Artes/Feed/')
    ano = date.today().year
    return render_template('GaleriaArtes.html', ano=ano, artesStorie=artesStorie, artesFeed=artesFeed)


# Rota para página de vídeos
@app.route('/GaleriaVideo')
def galeriaVideo():
    # Variáveis que recebem os arqiovos de vídeo e envia eles para a página html
    Reels = listdir('app/static/images/Videos/Reels')
    Eventos = listdir('app/static/images/Videos/Eventos')
    ano = date.today().year
    return render_template('GaleriaVideo.html', ano=ano, Reels=Reels, Eventos=Eventos)


# Rota para a página de Fotografia
@app.route('/GaleriaFotos')
def galeriafotos():
    # Variável que recebe os arquivos da pasta de imagem e envia eles para a página html
    nextImg = [f for f in listdir('app/static/images/Fotos/') if f.endswith(('.png', '.jpg', '.jpeg', '.JPG'))]
    images = listdir('app/static/images/Fotos/')
    ano = date.today().year
    return render_template('GaleriaFotos.html', ano=ano, images=images, nextImg=nextImg)


# Página de site (Ainda em construção)
@app.route('/GaleriaSites')
def galeriasite():
    ano = date.today().year
    return render_template('GaleriaSites.html', ano=ano)

