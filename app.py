from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def read_credentials():
    credentials = {}
    with open('credentials.txt', 'r') as file:
        for line in file:
            login, password = line.strip().split(',')
            credentials[login] = password
    return credentials

def check_login(login, password, credentials):
    if login in credentials and credentials[login] == password:
        return True
    return False

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    credentials = read_credentials()
    login = request.form['username']
    password = request.form['password']

    if check_login(login, password, credentials):
        return redirect('/success')
    else:
        return redirect('/failure')

@app.route('/success')
def success():
    return "Login successful!"

@app.route('/failure')
def failure():
    return "Invalid credentials!"

if __name__ == '__main__':
    app.run()
