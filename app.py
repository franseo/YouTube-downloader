from flask import Flask, request, flash, render_template, send_file, Response, redirect

from pytube import YouTube
import time
import os

app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

def bajarVideo(video):
    """ Borrar vídeos de la carpeta y descarga el vídeo de YouTube """
    d = "videos"
    for path in os.listdir(d):
        full_path = os.path.join(d, path)
        if os.path.isfile(full_path):
            os.remove(full_path)
    yt = YouTube(video)
    ys = yt.streams.get_highest_resolution()
    ys.download(output_path='videos')
    bajar = yt.title
    return bajar

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def formu():
    link = request.form['text']
    bajarv = bajarVideo(link)
    flash(bajarv)
    return render_template('index.html')

@app.route('/getVideo')
def getVideo():
    d = "videos"
    for path in os.listdir(d):
        full_path = os.path.join(d, path)
        if os.path.isfile(full_path):
            archivo = full_path
    return send_file(archivo, as_attachment=True)

app.run(debug=True)