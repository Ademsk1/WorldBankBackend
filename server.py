from flask import Flask, current_app, jsonify, request
from UserAccounts.UserAccountsAPI import *
from flask_cors import CORS
from world_bank_connect.worldbank_connect import *


app = Flask(__name__)
CORS(app, origins='https://localhost:3000')


@app.route('/get_user', methods=['GET', 'POST'])
def getting_user():
    if (request.method == 'POST'):
        data = request.json
        return get_user_data(data)


@app.route('/create_user', methods=['GET', 'POST'])
def creating_user():
    if (request.json == 'POST'):
        data = request.json
        return create_user(data)


@app.route('/general', methods=['GET'])
def general_info():
    return get_general_info()


@app.route('/search', methods=['POST'])
def search_query():
    return search()


if __name__ == '__main__':
    app.run(debug=True)
