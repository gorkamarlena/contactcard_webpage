from flask import render_template
from flask import Flask
from flask import request, redirect

app = Flask(__name__)

@app.route('/')
def hello():
    my_name = "Marlena"
    return f'Hello, {my_name}!'

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
   if request.method == 'GET':
       return render_template("contact.html")
   elif request.method == 'POST':
       return redirect("/")

@app.route('/mypage/me')
def me():
    return render_template("me.html")