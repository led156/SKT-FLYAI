from flask import Flask, render_template, request, redirect, session
from werkzeug.utils import secure_filename
from sqlalchemy import create_engine, text

app = Flask(__name__)
# app = Flask(__name__, static_url_path='/static')

app.config.from_pyfile('config.py')
database = create_engine(app.config['DB_URL'], encoding = "utf-8")
app.database = database

app.config['SECRET_KEY'] = 'keys'

@app.route('/')
def index():
    if not session.get('ss_id'): 
        ss_name = ""
        ss_img = ""
        return redirect('/login')
    else:
        ss_name = session['ss_name']
        
    return render_template('index.html', ss_id=session.get('ss_id'), ss_name = session.get('ss_name'), ss_img = session.get('ss_img'))

@app.route('/list')
def get_list():
    user = app.database.execute(text("""select name, age, img, num, userid from mem;""")).fetchall()
    
    return render_template('list.html', user = user, ss_id=session.get('ss_id'))

@app.route('/delete')
def delete():
    num = request.args.get('num')

    if session['ss_id'] == 'admin':
        sql = f"delete from mem where num = {num}';"
    else:
        sql = f"delete from mem where num = {num} and userid = '{session['ss_id']}';"

    app.database.execute(text(sql)).lastrowid

    return redirect('/list')

@app.route('/edit', methods = ['GET', 'POST'])
def edit():
    if request.method == 'GET':
        num = request.args.get('num')
        sql = f"""select * from mem where num = '{num}'"""
        user = app.database.execute(text(sql)).fetchone()

        return render_template('edit.html', user = user)
    else:
        userid = request.form['userid']
        username = request.form['username']
        usersex = request.form['sex']
        usertel = request.form['tel']
        userpost = request.form['post_num']
        userage = request.form['age']
        useraddress = request.form['address']

        num = request.form['num']
        
        # DB 인젝션 공격이 있는지
        # 이미 가입되어 있는지 확인
        # DB 저장

    
        f = request.files['img1']
        
        if f:
            f.save("static/upload/" + secure_filename(f.filename))
            sql_img = ", img = '%s'" % (f.filename)
        else:
            sql_img = ""

        new_user_id = app.database.execute(text(f"""
            update mem set
                userid='{userid}',
                name='{username}',
                sex='{usersex}',
                post_num='{userpost}',
                address='{useraddress}',
                tel='{usertel}',
                age='{userage}'
                {sql_img}'
                where num = {num}""")).lastrowid


        return redirect('/list')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if not session.get('ss_id'): 
        if request.method == 'GET':
            return render_template('login.html')

        elif request.method == 'POST':
            userid = request.form['userid']
            userpw = request.form['userpw']

            user = app.database.execute(text("""
                select name, img from mem where 
                userid = :userid and passwd = SHA2(:userpw, 256);"""), {
                    'userid' : userid,
                    'userpw' : userpw
                }).fetchone()
            if user['name'] == "":
                return render_template('login.html', msg='아이디 또는 비밀번호가 틀립니다.')
            else :
                session['ss_id'] = userid
                session['ss_name'] = user['name']
                session['ss_img'] = user['img']
                
                return redirect('/')
    else :
        return redirect('/')
        


@app.route('/logout')
def logout():
    session['ss_id'] = False
    session['ss_name'] = False
    return redirect('/')



@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'GET':
        return render_template('register.html')

    elif request.method == 'POST':
        userid = request.form['userid']
        userpw = request.form['userpw']
        username = request.form['username']
        usersex = request.form['sex']
        usertel = request.form['tel']
        userpost = request.form['post_num']
        userage = request.form['age']
        useraddress = request.form['address']
        
        # DB 인젝션 공격이 있는지
        # 이미 가입되어 있는지 확인
        # DB 저장

        f = request.files['img1']
        userimg = ""
        if f:
            f.save("static/upload/" + secure_filename(f.filename))
            userimg = "static/upload/" + secure_filename(f.filename)

        new_user_id = app.database.execute(text("""
            INSERT INTO mem(
                userid,
                passwd,
                name,
                sex,
                post_num,
                address,
                tel,
                age,
                img
            ) VALUES (
                :userid,
                SHA2(:userpw, 256),
                :username,
                :usersex,
                :userpost,
                :useraddress,
                :usertel,
                :userage,
                :userimg
            )
        """), {
            'userid' : userid,
            'userpw' : userpw,
            'username' : username,
            'usersex' : usersex,
            'userpost' : userpost,
            'useraddress' : useraddress,
            'usertel' : usertel,
            'userage' : int(userage),
            'userimg' : userimg
        }).lastrowid
        


        return redirect('/login?join=y')



# @app.route("/insert")
# def insertdb():
#     app.database.execute(text("""
#     insert into mem set
#     id = '1lsang',
#     name = '1lsangPark',
#     sex = 'M',
#     post_num = '12345',
#     address = 'seoul',
#     tel = '010-1234-5678',
#     age = 10;""")).lastrowid
#     return "Insert DB OK"

    
if __name__ == '__main__':
    app.run(debug=True)
