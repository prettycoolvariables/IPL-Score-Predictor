from flask import Flask, render_template, request, url_for, redirect,session 
import pandas as pd
import numpy as np
import pickle
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


app = Flask(__name__)
app.secret_key = 'your_secret_key'

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

client = MongoClient("mongodb+srv://aleenamariarajesh:nI7ya8Sf8W5INqlY@cluster0.ik10nn7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",server_api=ServerApi('1'))
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
            session['username'] = username
            # Authentication successful, redirect to home page
            return redirect(url_for('match'))
        else:
            # Authentication failed, redirect back to login page with error message
            return render_template('loginpage.html', error='Invalid username or password')
    else:
        return render_template('loginpage.html')

@app.route('/match')
def match():
    if 'username' not in session:  # Check if user is logged in
        return redirect(url_for('login'))
    return render_template("matchpage.html")

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove username from session
    return redirect(url_for('login'))

def score_predict(venue,innings,ball,batting_team, bowling_team,runs,cruns,cwicket):
  bat=[]
  bowl=[]
  stadium=[]
  #venue
  if venue == 'Arun Jaitley Stadium, Delhi':
    stadium=[1,0,0,0,0,0,0,0,0,0,0]
  elif venue == 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam':
    stadium=[0,1,0,0,0,0,0,0,0,0,0]
  elif venue == 'Eden Gardens, Kolkata':
    stadium=[0,0,1,0,0,0,0,0,0,0,0]
  elif venue == 'Himachal Pradesh Cricket Association Stadium, Dharamsala':
    stadium=[0,0,0,1,0,0,0,0,0,0,0]
  elif venue == 'MA Chidambaram Stadium, Chennai':
    stadium=[0,0,0,0,0,1,0,0,0,0,0]
  elif venue == 'M.Chinnaswamy Stadium, Bengaluru':
    stadium=[0,0,0,0,1,0,0,0,0,0,0]
  elif venue == 'Narendra Modi Stadium, Ahmedabad':
    stadium=[0,0,0,0,0,0,1,0,0,0,0]
  elif venue == 'Punjab Cricket Association IS Bindra Stadium, Mohali':
    stadium=[0,0,0,0,0,0,0,1,0,0,0]
  elif venue == 'Rajiv Gandhi International Stadium, Hyderabad':
    stadium=[0,0,0,0,0,0,0,0,1,0,0]
  elif venue == 'Sawai Mansingh Stadium, Jaipur':
    stadium=[0,0,0,0,0,0,0,0,0,1,0]
  elif venue == 'Wankhede Stadium, Mumbai':
    stadium=[0,0,0,0,0,0,0,0,0,0,1]
      
  # Batting Team
  if batting_team == 'Chennai Super Kings':
    bat=[1,0,0,0,0,0,0,0,0,0]
  elif batting_team == 'Delhi Capitals':
    bat=[0,1,0,0,0,0,0,0,0,0]
  elif batting_team == 'Gujarat Titans':
    bat= [0,0,1,0,0,0,0,0,0,0]
  elif batting_team == 'Kolkata Knight Riders':
    bat=[0,0,0,1,0,0,0,0,0,0]
  elif batting_team == 'Lucknow Super Giants':
    bat=[0,0,0,0,1,0,0,0,0,0]
  elif batting_team == 'Mumbai Indians':
    bat=[0,0,0,0,0,1,0,0,0,0]
  elif batting_team == 'Punjab Kings':
    bat= [0,0,0,0,0,0,1,0,0,0]
  elif batting_team == 'Rajasthan Royals':
    bat= [0,0,0,0,0,0,0,1,0,0]
  elif batting_team == 'Royal Challengers Bangalore':
    bat=[0,0,0,0,0,0,0,0,1,0]
  elif batting_team == 'Sunrisers Hyderabad':
    bat=[0,0,0,0,0,0,0,0,0,1]
      
  # Bowling Team
  if batting_team == 'Chennai Super Kings':
    bowl=[1,0,0,0,0,0,0,0,0,0]
  elif batting_team == 'Delhi Capitals':
    bowl=[0,1,0,0,0,0,0,0,0,0]
  elif batting_team == 'Gujarat Titans':
    bowl= [0,0,1,0,0,0,0,0,0,0]
  elif batting_team == 'Kolkata Knight Riders':
    bowl=[0,0,0,1,0,0,0,0,0,0]
  elif batting_team == 'Lucknow Super Giants':
    bowl=[0,0,0,0,1,0,0,0,0,0]
  elif batting_team == 'Mumbai Indians':
    bowl=[0,0,0,0,0,1,0,0,0,0]
  elif batting_team == 'Punjab Kings':
    bowl= [0,0,0,0,0,0,1,0,0,0]
  elif batting_team == 'Rajasthan Royals':
    bowl= [0,0,0,0,0,0,0,1,0,0]
  elif batting_team == 'Royal Challengers Bangalore':
    bowl=[0,0,0,0,0,0,0,0,1,0]
  elif batting_team == 'Sunrisers Hyderabad':
    bowl=[0,0,0,0,0,0,0,0,0,1]

  array=stadium+[innings,ball]+bat+bowl+[runs,cruns,cwicket]  
  prediction_array = np.array([array]) 
  print(prediction_array)
  pred = model.predict(prediction_array)
  return int(round(pred[0]))


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        venue=[int(request.form['stadium'])]
        inn=[1]
        ball=[float(request.form['currentBall'])]
        batting=[request.form['battingteam']]
        bowling=[request.form['bowlingteam']]
        runs=[float(request.form['currentScore'])]
        cruns=[float(request.form['currentScore'])]
        cwicket=[int(request.form['currentWickets'])]
        venue='Arun Jaitley Stadium, Delhi'
        batting='Delhi Capitals'
        bowling='Gujarat Titans'
        inn=1
        ball=4.5
        runs=0
        cruns=38
        wicket=0
        cwicket=2
        output=score_predict(venue,inn,ball,batting, bowling,runs,cruns,cwicket)
        print(output)
        return render_template('predictpage.html', score=output)

# if __name__ == "__main__":
#     app.run(debug=True)

import os
if __name__ == "_main_":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)




