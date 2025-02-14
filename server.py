from flask import Flask, render_template, send_from_directory, redirect, url_for, session, request, abort
import os
import json

app = Flask(__name__)
app.secret_key = 'random_secret_key'

# Load users from JSON file
with open('users.json') as f:
    users = json.load(f)

base_directory = '/media/amir/F62CC2BE2CC2795F/'  # Default directory

@app.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    try:
        files = os.listdir(base_directory)
        file_info = [{"name": f, "is_dir": os.path.isdir(os.path.join(base_directory, f))} for f in files]
    except FileNotFoundError:
        return "Directory not found. Please ensure the directory exists."
    return render_template('index.html', files=file_info, current_directory='')

@app.route('/files/<path:subpath>')
def files(subpath):
    if 'user' not in session:
        return redirect(url_for('login'))
    file_path = os.path.join(base_directory, subpath)
    if os.path.isdir(file_path):
        try:
            files = os.listdir(file_path)
            file_info = [{"name": f, "is_dir": os.path.isdir(os.path.join(file_path, f))} for f in files]
            return render_template('index.html', files=file_info, current_directory=subpath)
        except FileNotFoundError:
            return abort(404, description="Directory not found")
    else:
        try:
            return send_from_directory(os.path.dirname(file_path), os.path.basename(file_path))
        except FileNotFoundError:
            return abort(404, description="File not found")

@app.route('/welcome')
def welcome():
    return 'Welcome to the File Hosting Service'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for('index'))
        else:
            return 'Invalid credentials, please try again.'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('welcome'))

if __name__ == '__main__':
    app.run(debug=True)
