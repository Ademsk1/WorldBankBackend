from flask import Flask, current_app, jsonify, request
from UserAccounts.UserAccountsAPI import *
from flask_cors import CORS


app = Flask(__name__)
CORS(app, origins='https://localhost:3000')

@app.route('/create_user', methods = ['GET','POST'])
def getting_user():
    if(request.json == 'GET'):  
        return log_in()
    elif(request.json == 'POST'):
        return create_user()



if __name__ == '__main__':
    app.run(debug=True)
