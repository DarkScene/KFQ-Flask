from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/method/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Post'
    else:
        return 'Get'

if __name__ == '__main__':
    app.run(debug=True, port=8089)