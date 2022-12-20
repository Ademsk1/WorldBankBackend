from flask import Flask, current_app, jsonify, request
from UserAccounts.UserAccountsAPI import *


app = Flask(__name__)
@app.route('/user')
def getting_user():
    return get_user()



if __name__ == '__main__':
    app.run(debug=True)
