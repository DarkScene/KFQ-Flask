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
@app.route('/fileUpload', methods=['POST'])
def fileUpload():
    if request.method == 'POST':
        f = request.files['file']
        # 저장할 경로 + 파일명
        dirname = os.path.dirname(__file__) + '/files/' + f.filename
        print(dirname)
        f.save(dirname)
    return redirect('/files')

@app.route('/files')
def list_files():
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        # file이면 추가
        if os.path.isfile(path):
            files.append(filename)
    return render_template('list.html', files=files)

@app.route('/files/<path:path>')
def get_file(path):
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)

@app.route('/resume', methods=['GET','POST'])
def resume():
    if request.method == 'GET':
        return render_template('resume.html')
    else:
        result = request.form

        f = request.files['file']
        # 저장할 경로 + 파일명
        dirname = os.path.dirname(__file__) + '/files/' + f.filename
        print(dirname)
        f.save(dirname)
    return render_template('/files', result = result, file = f.filename)

if __name__ == '__main__':
    app.run(debug=True, port=8089)