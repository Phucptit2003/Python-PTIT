from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__, template_folder='html_templates')

#Trang Home
@app.route('/')
def home():
    return render_template('home.html')

# Trang Đăng ký
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        #Kiểm tra xem tên tồn tại hay chưa
        with open('DB.txt', 'r') as file:
            for line in file:
                stored_username, _, _ = line.strip().split(';')
                if stored_username == username:
                    return "Tài khoản đã tồn tại, Vui lòng <a href='/register'>đăng ký tài khoản khác</a>."

        with open('DB.txt', 'a') as file:
            file.write(f'{username};{password};{email}\n')
            return "Đăng ký thành công. Bạn có thể <a href='/login'>đăng nhập</a> hoặc <a href='/'>quay về trang chủ</a>."
    
    return render_template('register.html')


# Trang Đăng nhập
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Đọc thông tin 
        with open('DB.txt', 'r') as file:
            for line in file:
                stored_username, stored_password, _ = line.strip().split(';')
                if stored_username == username and stored_password == password:
                    return redirect(url_for('login_success'))
        return redirect(url_for('login_error'))

    return render_template('login.html')

# Trang Đăng nhập thành công
@app.route('/login_success')
def login_success():
    return "Bạn đã đăng nhập thành công. <a href='/'>Quay về trang chủ</a>."

# Trang Đăng nhập không thành công
@app.route('/login_error')
def login_error():
    return "Bạn đã nhập sai tài khoản hoặc mật khẩu. Nếu bạn chưa có tài khoản, <a href='/register'>hãy đăng ký</a> hoặc <a href='/login'>Quay lại trang đăng nhập</a>."


if __name__ == '__main__':
    app.run(debug=True)
