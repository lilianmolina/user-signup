from flask import Flask, request, redirect
import cgi
import os
import jinja2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('index.html')
    return template.render()

@app.route("/welcome")
def welcome():
    return "<h1>Welcome </h1>"

@app.route("/", methods=['POST'])
def validate():
    username = request.form['usernamehtml']
    password = request.form['passwordhtml']
    verify = request.form['verifyhtml']
    email = request.form['emailhtml']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    req_char = 0
    req_char_two = 0

    template = jinja_env.get_template('index.html')

    if len(username) < 3 or len(username) > 20:
        username_error = "That is not a valid username"

    if len(password) < 3 or len(password) > 20:
        password_error = "That is not a valid password"

    if password != verify:
        verify_error = "Passwords don't match"
    
    if len(email) > 0:
        for character in email:
            if character == "@":
                req_char += 1
            if character == ".":
                req_char_two += 1
        
        if req_char != 1 or req_char_two != 1:
            email_error = "That's not a valid email"

    if not username_error and not password_error and not verify_error and not email_error:
        return redirect('/welcome?name={0}'.format(username))

    return template.render(usernamehtml=username, passwordhtml=password, verifyhtml=verify, 
    emailhtml=email, username_error_html=username_error, password_error_html=password_error, 
    verify_error_html=verify_error, email_error_html=email_error)



if __name__ == '__main__':
    app.run()
