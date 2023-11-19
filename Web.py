from flask import Flask, render_template, request, redirect, url_for, session, flash



import csv
import os
import time

app = Flask(__name__, template_folder='html_templates')
app.secret_key = '12345'

# Trang chủ
@app.route('/')
def home():
    return render_template('home.html')

db_file = 'DB.csv'
feedback_file = 'feedback.csv'


def read_users():
    users = []
    if os.path.exists(db_file):
        with open(db_file, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if len(row) == 3:  # Kiểm tra xem có đủ 3 trường dữ liệu
                    users.append({'username': row[0], 'password': row[1], 'email': row[2]})
    return users

# Ghi thông tin người dùng vào DB.csv
def write_user(username, password, email):
    with open(db_file, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([username, password, email])

# Đọc danh sách phản hồi từ feedback.csv
def read_feedback():
    feedback = []
    if os.path.exists(feedback_file):
        with open(feedback_file, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if len(row) == 3:  
                    feedback.append({'username': row[0], 'feedback': row[1], 'time': row[2]})
    return feedback


def write_feedback(username, feedback):
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    with open(feedback_file, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([username, feedback, current_time])

# Trang đăng ký
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        users = read_users()
        for user in users:
            if user['username'] == username:
                return "Tài khoản đã tồn tại. Bạn vui lòng  <a href='/register'>đăng ký tài khoản khác</a> hoặc <a href='/login'>đăng nhập</a> hoặc <a href='/'>quay về trang chủ</a>."

        write_user(username, password, email)
        return "Đăng ký thành công. Bạn có thể <a href='/login'>đăng nhập</a> hoặc <a href='/'>quay về trang chủ</a>."
    return render_template('register.html')


# Trang đăng nhập
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = read_users()
        for user in users:
            if user['username'] == username and user['password'] == password:
                session['logged_in'] = True
                session['username'] = username
                flash('Đăng nhập thành công', 'success')
                return redirect(url_for('feedback'))
        
        flash('Sai thông tin đăng nhập', 'error')
    return render_template('login.html')

# Trang phản hồi
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    feedback_data = read_feedback()

    if request.method == 'POST':
        feedback_text = request.form['feedback']
        write_feedback(session['username'], feedback_text)
        return redirect(url_for('success', message="Gửi phản hồi thành công"))

    return render_template('feedback.html', feedback_data=feedback_data)

# Trang thông báo thành công
@app.route('/success')
def success():
    message = request.args.get('message', '')
    return render_template('success.html', message=message)




if __name__ == '__main__':
    app.run(debug=True)
