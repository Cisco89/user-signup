from flask import Flask, request, render_template, redirect
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

def validate_passwords(value_1, value_2):
    if value_1 == value_2:
        return True

    return False


@app.route("/")
def index():
    return render_template(
        'user-signup.html', 
        title='User SignUp'
        )

@app.route("/", methods=['POST'])
def welcome():
    username = request.form['user_name']
    password = request.form['password']
    validate_password = request.form['validate_password']
    email = request.form['email']

    # error messages
    username_error = ''
    password_error = ''
    validate_password_error = ''
    email_error = ''

    if not validate_passwords(password, validate_password):
        validate_password_error = 'Passwords must match!'

    if not validate_password_error:
        return render_template(
            'welcome.html', 
            title='Welcome', 
            username=username,
            )
    else:
        return render_template(
            'user-signup.html',
            title='User SignUp',
            username=username,
            username_error=username_error,
            password_error=password_error,
            validate_password_error=validate_password_error,
            )

app.run()
