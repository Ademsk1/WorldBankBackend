from flask import Flask, current_app, jsonify, request
from UserAccounts.UserAccountsAPI import *
from flask_cors import CORS


app = Flask(__name__)
CORS(app, origins='https://localhost:3000')

@app.route('/get_user', methods = ['GET', 'POST'])
def getting_user(): 
        if(request.method == 'POST'):
            data = request.json
            return get_user_data(data)




@app.route('/create_user', methods= ['GET','POST'])
def creating_user():
    if(request.json == 'POST'):
        data = request.json
        return create_user(data)




if __name__ == '__main__':
    app.run(debug=True)
