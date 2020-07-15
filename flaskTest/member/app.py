from flask import Flask, request, render_template, redirect
import pymysql

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def formTest():
    return render_template('form.html')

@app.route('/usersform', methods=['GET','POST'])
def usersform():
    if request.method == 'GET':
        return render_template('usersform.html')
    else: # request.method == 'POST'
        userid = request.form.get('userid')
        userpw = request.form.get('userpw')
        username = request.form.get('username')
        userage = request.form.get('userage')
        usermail = request.form.get('usermail')
        useradd = request.form.get('useradd')
        usergender = request.form.get('usergender')
        usertel = request.form.get('usertel')

        try:
            connection=pymysql.connect(host='localhost',
                            user='root',
                            password='qwer1234',
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
            
            with connection.cursor() as cursor:
                sql='''
                    insert into users values(%s, %s, %s, %s, %s, %s, %s, %s)
                '''
                data = (userid, userpw, username, userage, usermail, useradd, usergender, usertel)
                cursor.execute(sql, data)
                connection.commit()

        finally:
            connection.close()
    
    return redirect('/list')

@app.route('/list')
def list():
    connection=pymysql.connect(host='localhost',
                            user='root',
                            password='qwer1234',
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
            
    try:
        with connection.cursor() as cursor:
            sql="select * from users"
            cursor.execute(sql)
            result = cursor.fetchall()

    finally:
        connection.close()

    return render_template('list.html', list=result)

@app.route('/content/<userid>')
def content(userid):
    connection=pymysql.connect(host='localhost',
                            user='root',
                            password='qwer1234',
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    
    try:
        with connection.cursor() as cursor:
            sql="select * from users where userid=%s"
            cursor.execute(sql, userid)
            result = cursor.fetchone()
            print(result)

    finally:
        connection.close()
    
    return render_template('content.html', list = result)

@app.route('/updateform/<userid>', methods=['GET'])
def updateformget(userid):
    connection=pymysql.connect(host='localhost',
                            user='root',
                            password='qwer1234',
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql="select * from users where userid=%s"
            cursor.execute(sql, userid)
            result = cursor.fetchone()
    finally:
        connection.close()
    
    return render_template('updateform.html', list=result)

@app.route('/updateform', methods=['POST'])
def updateformpost():
    connection=pymysql.connect(host='localhost',
                            user='root',
                            password='qwer1234',
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

    userid = request.form.get('userid')
    userpw = request.form.get('userpw')
    username = request.form.get('username')
    userage = request.form.get('userage')
    usermail = request.form.get('usermail')
    useradd = request.form.get('useradd')
    usergender = request.form.get('usergender')
    usertel = request.form.get('usertel')

    try:
        with connection.cursor() as cursor:
            sql='''
                update users
                set
                userpw=%s,
                username=%s,
                userage=%s,
                usermail=%s,
                useradd=%s,
                usergender=%s,
                usertel=%s
                where userid=%s;
            '''
            data = (userpw, username, userage, usermail, useradd, usergender, usertel, userid)
            cursor.execute(sql, data)
            connection.commit()
    finally:
        connection.close()
    
    return redirect('/list')

@app.route('/deleteform/<userid>')
def deleteformget(userid):
    connection=pymysql.connect(host='localhost',
                            user='root',
                            password='qwer1234',
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql="delete from users where userid=%s"
            cursor.execute(sql, userid)
            connection.commit()
    finally:
        connection.close()
    
    return redirect('/list')


if __name__ == '__main__':
    app.run(debug=True)