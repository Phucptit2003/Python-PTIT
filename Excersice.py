from flask import Flask, render_template, request, redirect, url_for, session, flash
import csv
import os
import time

app = Flask(__name__, template_folder='html_templates')


# Đường dẫn tới các file CSV
db_file = 'DB.csv'
feedback_file = 'feedback.csv'

# Đọc danh sách người dùng từ DB.csv vào một danh sách
def read_users():
    users = []
    if os.path.exists(db_file):
        with open(db_file, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
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
                feedback.append({'username': row[0], 'feedback': row[1], 'time': row[2]})
    return feedback

# Ghi phản hồi vào feedback.csv
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
                flash('Tài khoản đã tồn tại', 'error')
                return redirect(url_for('register'))

        write_user(username, password, email)
        flash('Đăng ký thành công', 'success')
        return redirect(url_for('login'))
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
                flash('Đăng nhập thành công', 'success')
                return redirect(url_for('feedback'))
        
        flash('Sai thông tin đăng nhập', 'error')
    return render_template('login.html')

# Trang đăng xuất
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Đã đăng xuất', 'success')
    return redirect(url_for('login'))

# Trang phản hồi
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        feedback_text = request.form['feedback']
        write_feedback(session['username'], feedback_text)
        flash('Gửi phản hồi thành công', 'success')

    feedback_data = read_feedback()
    return render_template('feedback.html', feedback_data=feedback_data)

if __name__ == '__main__':
    app.run(debug=True)
