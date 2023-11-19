from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
bcrypt = Bcrypt(app)

# Danh sách người dùng lưu trữ trong bộ nhớ tạm thời
users = []

# Form đăng nhập
class LoginForm(FlaskForm):
    username = StringField('Tên người dùng', validators=[DataRequired()])
    password = PasswordField('Mật khẩu', validators=[DataRequired()])
    submit = SubmitField('Đăng nhập')

# Form đăng ký
class RegistrationForm(FlaskForm):
    username = StringField('Tên người dùng', validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Mật khẩu', validators=[DataRequired()])
    confirm_password = PasswordField('Xác nhận mật khẩu', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Đăng ký')

# Trang home giới thiệu
@app.route('/')
def home():
    return render_template('home.html')

# Trang Đăng nhập
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    login_successful = False
    login_error = False  # Thêm biến để kiểm tra lỗi đăng nhập
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = next((user for user in users if user['username'] == username), None)
        if user:
            if bcrypt.check_password_hash(user['password'], password):
                login_successful = True
                flash('Đăng nhập thành công!', 'success')
            else:
                login_error = True  # Đánh dấu lỗi đăng nhập
        else:
            login_error = True  # Đánh dấu lỗi đăng nhập
    return render_template('login.html', form=form, login_successful=login_successful, login_error=login_error)

# Trang Đăng ký
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    registration_successful = False  # Mặc định chưa đăng ký thành công
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        users.append({'username': username, 'password': hashed_password})
        registration_successful = True  # Đánh dấu đã đăng ký thành công
    return render_template('register.html', form=form, registration_successful=registration_successful)


if __name__ == '__main__':
    app.run(debug=True)
