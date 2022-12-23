from flask import Flask, current_app, jsonify, request
from UserAccounts.UserAccountsAPI import *
from flask_cors import CORS
from world_bank_connect.worldbank_connect import *
# test

app = Flask(__name__)
CORS(app, origins='http://localhost:3000')


@app.route('/get_user', methods=['GET', 'POST'])
def getting_user():
    if (request.method == 'GET'):
        return get_data()
    if (request.method == 'POST'):
        data = request.json
        return get_user_data(data)


@app.route('/create_user', methods=['GET', 'POST'])
def creating_user():
    if (request.method == 'POST'):
        data = request.json
        return create_user(data)


@app.route('/general', methods=['GET'])
def general_info():
    return get_general_info()


@app.route('/search', methods=['POST'])
def search_query():
    return search()

@app.route('/create_session', methods=['POST'])
def creating_user_session():
    data = request.json
    return create_user_session(data)

@app.route('/get_session', methods=['POST'])
def getting_user_session():
    data = request.json
    return get_user_session(data)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
