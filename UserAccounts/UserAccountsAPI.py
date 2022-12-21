from flask import jsonify
import bcrypt
from UserAccounts.connections import db_select, get_db_user_connection


conn_user_db = get_db_user_connection()
print(conn_user_db)


def create_user(data):
    check_stories1 = db_select(conn_user_db, 'select * from user_table')
    try:
        if not any(dictionary.get('username') == data[0]['name'] and compare_hashed_passwords(data[0]['password'], dictionary.get('salt'), dictionary.get('password')) for dictionary in check_stories1):
            hashed_result = (create_hash_password(data[0]['password']))
            send = db_select(conn_user_db, 'insert into user_table (username, password, type_id, salt) values (%s, %s, 1, %s) returning 1', ((data[0]['name']),(hashed_result[0]),(hashed_result[1])))
            return jsonify('user created')
        else:
            return jsonify('user is already in database')

            check_stories2 = db_select(conn_user_db, 'select * from user_table')
            return jsonify(check_stories2)
    except:
        return jsonify('Error creating account')

def get_user_data(data):
    try:
        check_stories1 = db_select(conn_user_db, 'select * from user_table')
        for user in check_stories1:
            if(user['username'] == data[0]['name'] and compare_hashed_passwords(data[0]['password'], user.get('salt'), user.get('password'))):
                check_stories2 = db_select(conn_user_db, 'select * from user_table where username=%s and password=%s', ((user['username']),(user['password'])))
                return jsonify(check_stories2)
        return jsonify('user was not found')
    except:
        return jsonify('Error Fetching User')

def get_data():
    check_stories1 = db_select(conn_user_db, 'select * from user_table')
    return jsonify(check_stories1)


def create_hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('UTF-8'), salt)
    return([hashed.decode('UTF-8'),salt.decode('UTF-8')])

def compare_hashed_passwords(inputted_password, salt, saved_password):
    return bcrypt.checkpw(inputted_password.encode('UTF-8'), saved_password.encode('UTF-8'))


