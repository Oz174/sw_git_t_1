#m1
#m1
from flask import Flask, render_template, request
app = Flask(__name__)
users=[]
@app.route("/")
def main_page():
    return render_template('index.html')


@app.route('/signup', methods= ['post'])
#even this is in java 
def sign_up():
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    if not user_exists(email=email, username=username, password=password):
        users.append(
            {
                'email': email,
                'username': username,
                'password': password
            }
        )
        return "<h3>New user has been created</h3>"
    else:
        return "<h3>This user already exists</h3>"

def changes():
    return 
def user_exists(email, username, password):
    #search for the user it's like FindOne in js 
    for user in users:
        if user['username'] == username or user['email']==email:
            return True
    return False

app.run(debug=True, host='0.0.0.0')
