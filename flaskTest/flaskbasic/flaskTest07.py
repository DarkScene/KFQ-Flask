from flask import Flask, make_response, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/setcookie', methods=['POST','GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['name']
        res = make_response("Create cookie!!")
        res.set_cookie("userID", user)
        return res

@app.route('/getcookie')
def getcookie():
    return request.cookies.get('userID')

if __name__ == '__main__':
    app.run()