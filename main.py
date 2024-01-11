from flask import Flask,render_template, redirect, url_for, request
from s3details import s3DownloadUpload
 
app = Flask(__name__)
'''
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/insert')
def insertDetails():
    return render_template('index.html', message='Hello, Flask!')

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name
'''

@app.route('/register', methods=['GET','POST'])
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    emailId = request.form['name']
    s3DownloadUpload(emailId)
    return f'Appreciate your interest, an email has been sent to {emailId}!'

@app.route('/registernew')
# def is normally how we define a function in python
def register():
 return render_template('register.html')

# main driver function
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
