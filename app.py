from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from sendemail import sendgridmail
import smtplib


app = Flask(__name__)
  
app.secret_key = 'a'
  
app.config['MYSQL_HOST'] = "remotemysql.com"
app.config['MYSQL_USER'] = ""
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "" 
mysql = MySQL(app)
@app.route('/')

def home():
	    return render_template('home.html')



@app.route('/login',methods =['GET', 'POST'])
def login():
    global userid
    msg = ''
   
  
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user WHERE username = % s AND password = % s', (username, password ),)
        account = cursor.fetchone()
        print (account)
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            userid=  account[0]
            session['username'] = account[1]
            msg = 'Logged in successfully !'
            
            msg = 'Logged in successfully !'
            return render_template('expense.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)

        


@app.route('/register', methods =['GET', 'POST'])
def registet():
    msg = ''
    if request.method == 'POST' :
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user WHERE username = % s', (username, ))
        account = cursor.fetchone()
        print(account)
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'name must contain only characters and numbers !'
        else:
            cursor.execute('INSERT INTO user VALUES (NULL, % s, % s, % s)', (username, email,password))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
            TEXT = "Hello "+username + ",\n\n"+ """Thanks for applying registring at smartinterns """ 
            message  = 'Subject: {}\n\n{}'.format("smartinterns Carrers", TEXT)
            #sendmail(TEXT,email)
            sendgridmail(email,TEXT)
            print(email)
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)





if __name__ == '__main__':
   app.run(host='0.0.0.0',debug = True,port = 5000)
   