from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

# http://127.0.0.1:8089/method/
@app.route('/method/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Post'
    else:
        return 'Get'

# http://127.0.0.1:8089/login?name=TaeHyeon 으로 접근 가능
@app.route('/login') # method는 자동으로 GET 방식
def login1():
    user = request.args.get('name')
    return "User %s"%user

@app.route('/login', methods=['POST'])
def login2():
    username = request.form['username']
    pw = request.form['password']
    return "Username: %s, PW: %s"%(username, pw)

if __name__ == '__main__':
    app.run(debug=True, port=8089)