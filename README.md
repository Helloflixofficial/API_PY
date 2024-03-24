HOW TO RUN THIS PYTHON API 

Installation..
```
git clone https://github.com/your_username/your_project.git 
``` 
```
cd your_project
```
```
pip install -r requirements.txt
```
```
python app.py
```







# Flask Cheat Sheet and Quick Reference

This document provides a quick reference guide for developing a Flask application. Below are the key components and features along with code snippets for each.

## Barebones App

```python
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)


# Routing
@app.route('/hello/<string:name>')
def hello(name):
    return 'Hello ' + name + '!'


# Allowed Request Methods
@app.route('/test', methods=['GET', 'POST'])  # Allows only GET and POST requests


# Configuration
app.config['CONFIG_NAME'] = 'config value'
app.config.from_envvar('ENV_VAR_NAME')


# Templates
from flask import render_template

@app.route('/')
def index():
    return render_template('template_file.html', var1=value1, ...)



# JSON Responses

from flask import jsonify

@app.route('/returnstuff')
def returnstuff():
    num_list = [1, 2, 3, 4, 5]
    num_dict = {'numbers': num_list, 'name': 'Numbers'}
    return jsonify({'output': num_dict})

# run the app
    python app.py


#Access Request Data
request.args['name'] #query string arguments
request.form['name'] #form data
request.method #request type
request.cookies.get('cookie_name') #cookies
request.files['name'] #files


#Redirect
from flask import url_for, redirect
@app.route('/home')
def home():
 return render_template('home.html')
@app.route('/redirect')
def redirect_example():
 return redirect(url_for('index')) #sends user to /home
#Abort

from flask import abort()
@app.route('/')
def index():
 abort(404) #returns 404 error
 render_template('index.html') #this never gets executed


#Set Cookie
from flask import make_response
@app.route('/')
def index():
 resp = make_response(render_template('index.html'))
 resp.set_cookie('cookie_name', 'cookie_value')
 return resp



#Session Handling
import session
app.config['SECRET_KEY'] = 'any random string' #must be set to use sessions
#set session
@app.route('/login_success')
def login_success():
 session['key_name'] = 'key_value' #stores a secure cookie in browser
 return redirect(url_for('index'))


#read session
@app.route('/')
def index():
 if 'key_name' in session: #session exists and has key
 session_var = session['key_value']
 else: #session does not exist

```

#Useful Plugins
```
Flask-PyMongo - http://readthedocs.org/docs/flask-pymongo/
```
```
Flask-SQLAlchemy - http://pypi.python.org/pypi/Flask-SQLAlchemy
```
```
Flask-WTF - http://pythonhosted.org/Flask-WTF/
```
```
Flask-Mail - http://pythonhosted.org/Flask-Mail/
```
FLask-RESTFul - https://flask-restful.readthedocs.org/
```
```
Flask-Uploads - https://flask-uploads.readthedocs.org/en/latest/
```
```
Flask-User - http://pythonhosted.org/Flask-User/
```
```
FLask-Login - http://pythonhosted.org/Flask-Login/
```