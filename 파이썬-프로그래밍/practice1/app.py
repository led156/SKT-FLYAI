from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename


app = Flask(__name__)
# app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == 'POST':
        userid = request.form['userid']
        userpw = request.form['userpw']

        if userid == 'admin' and userpw == '1234':
            return redirect('/')
        else:
            return render_template('login.html', msg='아이디 또는 비밀번호가 틀립니다') # template 에, 경고창 메시지 변수를 날림

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'GET':
        return render_template('register.html')

    elif request.method == 'POST':
        userid = request.form['userid']
        userpw = request.form['userpw']
        username = request.form['username']
        # DB 인젝션 공격이 있는지
        # 이미 가입되어 있는지 확인
        # DB 저장
        
        f = request.files['img1']
        f.save("./upload/" + secure_filename(f.filename))

        return redirect('/login?join=y')

    
if __name__ == '__main__':
    app.run(debug=True)
