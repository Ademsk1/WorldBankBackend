from flask import jsonify, Response
import json
import bcrypt
from UserAccounts.connections import db_select, get_db_user_connection



conn_user_db = get_db_user_connection()


def create_user(data): #handle empty input
    print(data)
    if(data[0]['name']=='' or data[0]['password']==''):
        return format_response(400, 'No inputs have been given')
    check_stories1 = db_select(conn_user_db, 'select * from user_table')
    try:
        if not any(dictionary.get('username') == data[0]['name'] and compare_hashed_passwords(data[0]['password'], dictionary.get('salt'), dictionary.get('password')) for dictionary in check_stories1):
            hashed_result = (create_hash_password(data[0]['password']))
            send = db_select(conn_user_db, 'insert into user_table (username, password, type_id, salt) values (%s, %s, 1, %s) returning 1', ((data[0]['name']),(hashed_result[0]),(hashed_result[1])))
            return format_response(200, 'user created')
        else:
            return format_response(400,'user is already in database')
    except:
        return format_response(500, 'Error creating account')

def get_user_data(data):
    try:
        check_stories1 = db_select(conn_user_db, 'select * from user_table')
        for user in check_stories1:
            if(user['username'] == data[0]['name'] and compare_hashed_passwords(data[0]['password'], user.get('salt'), user.get('password'))):
                check_stories2 = db_select(conn_user_db, 'select * from user_table where username=%s and password=%s', ((user['username']),(user['password'])))
                return jsonify(check_stories2), 200
        return format_response(404,'user was not found'), 404
    except:
        return format_response(500, 'Error Fetching User'), 500

def get_data():
    check_stories1 = db_select(conn_user_db, 'select * from user_table')
    return jsonify(check_stories1)


def create_hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('UTF-8'), salt)
    return([hashed.decode('UTF-8'),salt.decode('UTF-8')])


def compare_hashed_passwords(inputted_password, salt, saved_password):
    return bcrypt.checkpw(inputted_password.encode('UTF-8'), saved_password.encode('UTF-8'))

def format_response(code, message):
    return [{"status": code, "message": message}]


def create_user_session(data):
    user = ''.join(map(str,(data['user_id'])))
    countries = ' '.join(map(str,(data['country'])))
    indicator = ' '.join(map(str,(data['indicator'])))
    range = ' '.join(map(str,(data['range'])))

    if(db_select(conn_user_db, 'select exists(select 1 from sessions where user_id = %s)', ((user),))[0]['exists'] == True):
        db_select(conn_user_db, 'insert into sessions (user_id, countries, indicators, range, date) values (%s, %s, %s, %s, current_timestamp) returning id', ((user),(countries),(indicator),(range)))
        return format_response(200, 'new session created'), 200
    else:
        return format_response(500, 'error adding session'), 400

def get_user_session(data):
    find_user = db_select(conn_user_db, 'select type_id from user_table where id = %s', ((data['user_id']),))

    if(len(find_user) < 1):
        return [], 404
    elif(find_user[0]['type_id'] == 2):
        sessions_list = db_select(conn_user_db, 'select countries, indicators, range, username, date from sessions join user_table on sessions.user_id = user_table.id', ((data['user_id']),))
    elif(find_user[0]['type_id'] == 1):
        sessions_list = db_select(conn_user_db, 'select countries, indicators, range, date from sessions where user_id = %s', ((data['user_id']),))

    return sessions_list, 200


