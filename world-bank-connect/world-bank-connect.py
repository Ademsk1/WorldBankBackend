from flask import Flask, jsonify, request, send_file
import os
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
from flask_cors import CORS
import json

load_dotenv()
app = Flask(__name__)
CORS(app)

WB_DBNAME = os.getenv('WB_DBNAME')
WB_HOST = os.getenv('WB_HOST')
WB_PASSWORD = os.getenv('WB_PASSWORD')
WB_USERNAME = os.getenv('WB_USERNAME')


def validate_input(data):
    if len(data) == 0:
        return 'LENGTH=0'
    if len(data['indicator']) == 0:
        return 'NOINDICATORS'
    return 'None'


def get_params(search):
    country_params = tuple(search['country'])
    indicator_params = tuple(search['indicator'])
    params = tuple([country_params, indicator_params])
    return params


def get_bank_connection():
    try:
        conn = conn = psycopg2.connect(
            f"dbname={WB_DBNAME} user={WB_USERNAME} host={WB_HOST} port = 5432 password={WB_PASSWORD}")
        return conn
    except:
        return False


def query_bank_db(query, params=()):
    conn = get_bank_connection()
    if conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            # ((list of countries),(list of indicators))
            cursor.execute(query, params)
            data = cursor.fetchall()
        return data
    else:
        return 'No connection'


@app.route('/send_picture')
def send_picture():
    return send_file('../shaggy.jpeg')


@app.route('/search', methods=['POST'])
def search():
    error_handler = {'OKAY': '', 'NOINDICATORS': 'Please select an indicator',
                     'LENGTH=0': 'Please select countries and indicator(s)'}
    if request.method == 'POST':
        inp = jsonify({'country': ['Afghanistan', 'Albania'], 'indicator': [
                      'Merchandise imports from developing economies in South Asia (% of total merchandise imports)']})
        search = inp.json
        error_message = validate_input(search)
        query = "SELECT countryname,value,year FROM public.indicators WHERE countryname IN %s AND indicatorname IN %s"
        params = get_params(search)
        results = query_bank_db(query, params)
        response = {'results': results, 'errors': error_message}
        return jsonify(response)


@app.route('/general', methods=['GET'])
def get_general_info():
    conn = get_bank_connection()
    query_countries = "SELECT tablename from public.countries;"
    query_indicators = "SELECT indicatorname from public.series;"
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
        cursor.execute(query_countries)
        countries = cursor.fetchall()
        cursor.execute(query_indicators)
        indicators = cursor.fetchall()
        print(query_countries)
    return jsonify([countries, indicators])


if __name__ == '__main__':
    app.run(debug=True, port='5000')
