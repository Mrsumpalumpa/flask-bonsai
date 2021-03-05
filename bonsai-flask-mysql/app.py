from flask import Flask, render_template, url_for, flash, redirect, request
from forms import SignupForm, LoginForm
from flask_mysqldb import MySQL
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY']='2a3d5184366aead8d26664baacd4ae04'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Supadupa1234?'
app.config['MYSQL_DB'] = 'flask_bonsai'
mysql = MySQL(app)
posts=[
    {
        'name':'wtf',
        'lastname': 'omg',
        'title':'polno'
    },
    {
        'name':'pimpin',
        'lastname': 'og',
        'title':'erestonto'
    }
]

@app.route('/')
def home():
    return render_template('home.html',posts = posts, title = 'Home')

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if request.method == 'POST':
            emailp = request.form['email']
            passwordp = request.form['password'].encode('utf-8')
            pshash = bcrypt.hashpw(passwordp,bcrypt.gensalt()).decode('utf-8')
            cur = mysql.connection.cursor()
            cur.execute('SELECT email,password FROM users WHERE email = %s', [emailp])
            data = cur.fetchall()
            print (passwordp,data[0][1],pshash)
            if bcrypt.checkpw(passwordp,data[0][1].encode('utf-8')):
                flash('You have been logged in','success')
                return redirect(url_for('home'))             
            else:
                flash('Credentials does not match','danger')
                    
                
            
    return render_template('login.html', title = 'Log in', form = form)

@app.route('/signup', methods = ['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            password = request.form['password'].encode('utf-8')            
            pshash = bcrypt.hashpw(password,bcrypt.gensalt()).decode('utf-8')         
            print(username,email,pshash)
            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO users (username,email,password) VALUES (%s,%s,%s )',(username,email,pshash))
            mysql.connection.commit()    
        return redirect(url_for('home'))
    return render_template('signup.html', title= 'Sign up', form = form)

@app.route('/contact')
def contact():
    return render_template('contact.html', title ='Contact')



if __name__ == '__main__':
    app.run(port = 3000, debug= True)
