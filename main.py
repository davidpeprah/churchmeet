from flask import Flask, render_template, request, redirect, url_for, session
#from flask_mysqldb import MySQL
import mysql.connector
from datetime import timedelta


#import MySQLdb.cursors

import re

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = '0987uwuiherewjk23783@1'

# Enter your database connection details below
#app.config['MYSQL_HOST'] = 'mysqldb'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'MyS@lr00tdb'
#app.config['MYSQL_DB'] = 'churchhangout'

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)


# Intialize MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password='My$ql@r00t',
    database='churchmeet'
)
#mysql = MySQL(app)

# Covert tuple data from mysql into dictionary
def return_dict(row_headers, result):
    if type(result) is tuple:
        return dict(zip(row_headers, result))
    elif type(result) is list:
        data = []
        for x in result:
            data.append(dict(zip(row_headers, x)))
        return data
    else:
        return []

# http://localhost:5000/pythonlogin/ - this will be the login page, we need to use both GET and POST requests
@app.route('/login/', methods=['GET', 'POST'])
def login():
    
    # Output message if something goes wrong...
    msg = ''

    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']

    # Check if account exists using MySQL
        #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor = mydb.cursor()

        cursor.execute('SELECT * FROM members WHERE username = %s AND password = %s', (username, password,))
        
        # Get row headers
        row_headers = [x[0] for x in cursor.description]

        # Fetch one record and return result
        member = return_dict(row_headers, cursor.fetchone())

        # create a dictionary, using the headers as keys
        #member = dict(zip(row_headers,member))
        

    # If account exists in accounts table in out database
        if member:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['user_id'] = member['user_id']
            session['username'] = member['username']

            #Set session timer
            session.permanent = True

            # Redirect to home page
            return redirect(url_for('home'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'

    return render_template('index.html', msg=msg)

# http://localhost:5000/python/logout - this will be the logout page
@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   #session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))


# http://localhost:5000/pythinlogin/register - this will be the registration page, we need to use both GET and POST requests
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
                # Check if account exists using MySQL
        #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM members WHERE username = %s', (username,))
        account = cursor.fetchone()
        

        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO members VALUES (NULL, %s, %s, %s)', (username, password, email,))
            cursor.execute('INSERT INTO friends VALUES (NULL, %s, %s)', (username, username,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
            return redirect(url_for('login'))

    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)


# http://localhost:5000/pythinlogin/home - this will be the home page, only accessible for loggedin users
@app.route('/', methods=['POST', 'GET'])
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor = mydb.cursor()
        # User is loggedin show them the home page
        # query to get news feed
        # SELECT * FROM messages INNER JOIN friends ON user = auth WHERE friend=session['username']
        if request.method == 'POST' and 'text' in request.form:
           message = request.form['text']
           username = session['username']
           
           cursor.execute('INSERT INTO messages VALUES (NULL, %s, CURRENT_TIMESTAMP, %s)', (username, message,))
           mysql.connection.commit()
        
        cursor.execute('SELECT * FROM messages INNER JOIN friends ON friend = auth WHERE user=%s ORDER BY time DESC', (session['username'],))
        

        
        #news = []
        #n = cursor.fetchall()

        #for x in n:
         #   news.append(dict(zip(row_headers, x)))
        news = return_dict([x[0] for x in cursor.description], cursor.fetchall())

        #print(news)
        return render_template('home.html', username=session['username'], news=news)

    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


# http://localhost:5000/pythinlogin/profile - this will be the profile page, only accessible for loggedin users
@app.route('/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
        #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM members WHERE user_id = %s', (session['user_id'],))
        
        # row headers
        member = return_dict([x[0] for x in cursor.description], cursor.fetchone())
       
        # Show the profile page with account info
        return render_template('profile.html', account=member)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/members/')
@app.route('/members/<user_id>')
@app.route('/members/<action>/<user_id>')
def members(user_id=None, action=None):
    # List members on the platform
    if 'loggedin' in session:
       
       if not user_id:
          mutual = []
          fwers = []
          fwing = []

          #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
          cursor = mydb.cursor()
          
          cursor.execute('SELECT * FROM members WHERE user_id != %s', (session['user_id'],))
          members = return_dict([x[0] for x in cursor.description],cursor.fetchall())


          cursor.execute('SELECT user FROM friends WHERE friend = %s', (session['username'],))
          followers = return_dict([x[0] for x in cursor.description], cursor.fetchall())


          cursor.execute('SELECT friend FROM friends WHERE user = %s', (session['username'],))
          following = return_dict([x[0] for x in cursor.description], cursor.fetchall())

          if followers:
             for f in followers:
                fwers.append(f['user'])
          
          if following:
             for f in following:
                 fwing.append(f['friend'])

          for member in members:
             fw = False
             fl = False
             if member['username'] in fwers:
                fw = True
             if member['username'] in fwing:
                fl = True
             if fw and fl:
                mutual.append(member['username'])
                
          
          return render_template('members.html', members=members, fwers=fwers, fwing=fwing, mutual=mutual)

       elif action:
            #ursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor = mydb.cursor()

            cursor.execute('SELECT username FROM members WHERE user_id = %s', [user_id])
            member = cursor.fetchone()

            if member:
               if action == "add":
                  #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                  cursor = mydb.cursor()
                  cursor.execute('INSERT INTO friends VALUES (NULL, %s, %s)', (session['username'],member['username'],))
                  mysql.connection.commit()
               if action == "remove":
                  #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                  cursor = mydb.cursor()
                  cursor.execute('DELETE FROM friends WHERE user=%s AND friend=%s', (session['username'],member['username'],))
                  mysql.connection.commit()
            
            return redirect(url_for('members'))
       else:
          #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
          cursor = mydb.cursor()
          cursor.execute('SELECT * FROM members WHERE user_id = %s', [user_id])
          member = return_dict([x[0] for x in cursor.description],cursor.fetchone())
          
          

          return render_template('viewuser.html', member=member)


    return redirect(url_for('login'))


@app.route('/friends/')
@app.route('/friends/<action>/<friend>')
@app.route('/friends/<user_id>')
def friends(friend=None, action=None,user_id=None):
    
    if 'loggedin' in session:
       
         if not friend:

            #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor = mydb.cursor()
            cursor.execute('SELECT * FROM friends WHERE user = %s AND friend <> %s', (session['username'], session['username'],))
            friends = return_dict([x[0] for x in cursor.description], cursor.fetchall())

            return render_template('friends.html', friends=friends)
         
         elif action:
            #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor = mydb.cursor()
            cursor.execute('SELECT username FROM members WHERE username = %s', [friend])
            member = return_dict([x[0] for x in cursor.description], cursor.fetchone())

            if member:
               if action == "remove":
                  #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                  cursor = mydb.cursor()
                  cursor.execute('DELETE FROM friends WHERE user=%s AND friend=%s', (session['username'],member['username'],))
                  mysql.connection.commit()
               

         else:
            #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor = mydb.cursor()
            cursor.execute('SELECT * FROM members WHERE username = %s', (user_id,))
            
            friend = return_dict([x[0] for x in cursor.description], cursor.fetchone()) 
          
            return render_template('viewuser.html', member=friend)
 
         return redirect(url_for('friends'))

    return redirect(url_for('login'))

@app.route('/messages/')
@app.route('/messages/<user_id>', methods=['GET', 'POST']) 
def messages(user_id=None):

    if 'loggedin' in session:
       #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
       cursor = mydb.cursor()
       cur_user = session['username']
       #cursor.execute('SELECT username FROM members WHERE user_id=%s;', (user_id,))
       #receiver = cursor.fetchone()['username']

      

       if not user_id:
          
          
          cursor.execute('SELECT user_id, username FROM members INNER JOIN friends ON members.username = friends.user WHERE friends.friend = %s AND friends.user <> %s;', (cur_user, cur_user,))
          #frnds = cursor.fetchall()
          frnds = return_dict([x[0] for x in cursor.description],cursor.fetchall())

          return render_template('messages.html', friends=frnds)
       else:
          cursor.execute('SELECT username FROM members WHERE user_id=%s;', (user_id,))
          receiver = cursor.fetchone()['username']

          if request.method == 'POST' and 'text' in request.form:
              message = request.form['text']
              cursor.execute('INSERT INTO pmessages VALUES (NULL, %s, %s, CURRENT_DATE(), %s, NULL);', (cur_user, receiver, message,))
              mysql.connection.commit()
          
         

          cursor.execute('SELECT * FROM pmessages WHERE (sender=%s OR receiver=%s) AND (sender=%s OR receiver=%s);', (cur_user,cur_user, receiver, receiver,))
          pmessage = cursor.fetchall()

          return render_template('pmessages.html', username=receiver, cur_user=cur_user, pmessage=pmessage, user_id=user_id)
 
    else:
      return redirect(url_for('login'))


@app.route('/sendmessages/<username>',  methods=['GET', 'POST']) 
def sendmessages(username):
    if 'loggedin' in session:
        #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        
        cursor = mydb.cursor()
        cur_user = session['username']
        #cursor.execute('SELECT username FROM members WHERE user_id=%s;', (user_id,))
        receiver = username #cursor.fetchone()['username']

        if request.method == 'POST' and 'text' in request.form:
           message = request.form['text']
             
             
           cursor.execute('INSERT INTO pmessages VALUES (NULL, %s, %s, CURRENT_DATE(), %s, NULL);', (cur_user, receiver, message,))
           mysql.connection.commit()
           
           cursor.execute('SELECT * FROM pmessages WHERE (sender=%s OR receiver=%s) AND (sender=%s OR receiver=%s);', (cur_user,cur_user, receiver, receiver,))
           pmessage = cursor.fetchall()

           return render_template('pmessages.html', username=receiver, cur_user=cur_user, pmessage=pmessage)

    else:
      return redirect(url_for('login'))

if __name__ == '__main__':
   app.run(host='0.0.0.0', port='5000')
