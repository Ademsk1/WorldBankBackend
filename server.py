from flask import Flask, current_app, jsonify, request
from UserAccounts.UserAccountsAPI import *


app = Flask(__name__)
@app.route('/create_user', methods = ['GET','POST'])
def getting_user():
    if(request.json == 'GET'):  
        return log_in()
    elif(request.json == 'POST'):
        return create_user()



if __name__ == '__main__':
    app.run(debug=True)
