from flask import Flask, request, render_template, send_from_directory, redirect, url_for
import os

UPLOAD_DIRECTORY = os.path.dirname(__file__) + '/files'

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

# 파일 업로드 처리
@app.route('/fileUpload')
def fileUpload():
    if request.method == 'POST':
        f = request.files['file']
        # 저장할 경로 + 파일명
        dirname = os.path.dirname(__file__) + '/files' + f.filename
        print(dirname)
        f.save(dirname)
    return redirect('/files/')

if __name__ == '__main__':
    app.run(debug=True, port=8089)