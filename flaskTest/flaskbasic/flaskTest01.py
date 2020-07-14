# Flask 웹 어플리케이션 기본 골격

from flask import Flask, render_template, request
app = Flask(__name__) # 현재 파일의 파일명

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return "Yummy cakes!"

@app.route('/user/<username>/<path:p>')
def show_user_profile(username, p):
    return "User %s 경로는 %s"%(username, p)

if __name__ == '__main__':
    app.run(debug=True, port=8089)
    # debug=True : 변경사항이 있으면 자동으로 새로고침