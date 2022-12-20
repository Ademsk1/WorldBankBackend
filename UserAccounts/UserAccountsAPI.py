from flask import jsonify
import bcrypt
from UserAccounts.connections import db_select, get_db_user_connection


conn_user_db = get_db_user_connection()


def create_user(data): #check database first
    check_stories2 = db_select(conn_user_db, 'select * from user_types')
    return jsonify(check_stories2)

def log_in(): #check database first
    check_stories2 = db_select(conn_user_db, 'select * from user_types')
    return jsonify(check_stories2)
