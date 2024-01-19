from flask import Flask,render_template, redirect, url_for, request
from s3details import s3DownloadUpload
 
app = Flask(__name__)
context = ('../certificate/pmacademyy_com.crt', '../certificate/pmacademyy.com.key')

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers.add('Access-Control-Allow-Origin', '*')
    r.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    r.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('mainpage/index.html')

@app.route('/register', methods=['GET','POST'])
def form():
    return render_template('register/register.html')

@app.route('/submit', methods=['POST'])
def submit():
    emailId = request.form['name']
    s3DownloadUpload(emailId)
    print(emailId)
    return render_template('submit/index.html')
    #return f'Appreciate your interest, an email has been sent to {emailId}!'

@app.route('/testing', methods=['POST'])
def testing():
    fname = request.form['name']
    print(fname)
    return "Your name is "+fname 

'''
@app.route('/registernew')
# def is normally how we define a function in python
def register():
 return render_template('register.html')
'''

# main driver function
if __name__ == '__main__':
    #app.run(host='0.0.0.0', port="443", debug=True, ssl_context=context)
    #app.run(host='0.0.0.0', ssl_context=context, threaded=True, debug=True )
    app.run(host="pmacademyy.com")
