from flask import Flask, render_template, request, url_for, redirect 

app = Flask(__name__)

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient("mongodb+srv://admin:mongo@cluster0.imbdhgi.mongodb.net/",server_api=ServerApi('1'))
mongo = client["myDatabase"]
users_collection = mongo['users']

@app.route("/")
def home():
    return render_template("homepage.html")


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Get form data
        first_name = request.form['fname']
        last_name = request.form['lname']
        username = request.form['uname']
        email = request.form['email']
        password = request.form['password']
        
       
        
        # Insert user data into MongoDB
        user_data = {
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'email': email,
            'password': password
        }
        users_collection.insert_one(user_data)
        
        # Redirect to login page
        return redirect(url_for('login'))
    else:
        return render_template('createpage.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']
        
        
        
        # Validate user credentials against MongoDB
        user = users_collection.find_one({'username': username, 'password': password})
        if user:
            # Authentication successful, redirect to home page
            return redirect(url_for('match'))
        else:
            # Authentication failed, redirect back to login page with error message
            return render_template('loginpage.html', error='Invalid username or password')
    else:
        return render_template('loginpage.html')

# Route for the match page
@app.route('/match')
def match():
    return render_template("matchpage.html")

@app.route('/predict')
def predict():
    return render_template("predictpage.html")

if __name__ == "__main__":
    app.run(debug=True) 







