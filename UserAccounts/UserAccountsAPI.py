from flask import jsonify
from UserAccounts.connections import db_select, get_db_user_connection


conn_user_db = get_db_user_connection()


def get_user():
    check_stories2 = db_select(conn_user_db, 'select * from user_types')
    return jsonify(check_stories2)
