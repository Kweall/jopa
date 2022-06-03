import os
import time
import shutil
from moviepy.editor import *
from flask import Flask,flash,request,redirect, render_template
UPLOAD_FOLDER = 'static/uploads/'
app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # проверим, передается ли в запросе файл
        if 'file' not in request.files:
            # После перенаправления на страницу загрузки
            # покажем сообщение пользователю
            flash('Не могу прочитать файл')
            return redirect(request.url)
        file = request.files['file']
        # Если файл не выбран, то браузер может
        # отправить пустой файл без имени.
        if file.filename == '':
            flash('Нет выбранного файла')
            return redirect(request.url)
        if file:
            # сохраняем файл
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'video.mp4'))
            return redirect('http://127.0.0.1:5000/video')
    return render_template('main.html')
@app.route('/video', methods=['GET', 'POST'])
def video():
    if request.method == 'POST':
        os.system('python track.py --yolo_model best_3.pt --save-vid --save-txt')
        get_files = os.listdir('runs/track')
        print('C:/Users/Алексей/PycharmProjects/pobeda/runs/track/'+get_files[-1]+'/video.mp4')
        clip = VideoFileClip('runs/track/'+get_files[-1]+'/video.mp4')
        clip.write_videofile('static/video.mp4', fps=30)
        shutil.copyfile('runs/track/' + get_files[-1] + '/tracks/video.txt',
                        'static/video.txt')
        time.sleep(5)
        return redirect('http://127.0.0.1:5000/result')
    return render_template('video.html')
@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        os.system('python database.py')
    return render_template('result.html')
if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run()