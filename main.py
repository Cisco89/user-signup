from flask import Flask, request, render_template, redirect
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

# checking that password and validate password match each other
def validate_passwords(value_1, value_2):
    if value_1 == value_2:
        return True

    return False

# return error if there is a space of if length is invalid
def correct_entry(value):
    if ' ' in value:
        return False
    if 3 <= len(value) and 20 >= len(value):
        return True
    
    return False

# return error if there is space, invalid length, or missing characters "@" and "."
def correct_email_entry(email_entry):
    # checking if field was left blank(which is okay)
    if email_entry == '':
        return True
    # checking for special characters "@", "." 
    # and validating correct length by calling previouly created function 
    if '@' in email_entry and '.' in email_entry and correct_entry(email_entry):
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
    # providing values from the form data sent on POST method
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

    if not correct_entry(username):
        username_error = "Username cannot contain spaces and must consist of 3-20 characters!"

    if not correct_entry(password):
        password_error = "Password cannot contain spaces and must consist of 3-20 characters!"

    if not correct_email_entry(email):
        email_error = "Email cannot contain spaces and must consist of 3-20 characters and follow the format of an email address ex. someone@gmail.com"

    # checking there are no errors occuring
    # if error occurs stay in signup page, but keep username and display errors
    if not validate_password_error and not username_error and not password_error and not email_error:
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
            email_error=email_error,
            )

app.run()
