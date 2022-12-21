from flask import Flask, jsonify, request
import os
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
from flask_cors import CORS


load_dotenv()
app = Flask(__name__)
CORS(app)

WB_DBNAME = os.getenv('WB_DBNAME')
WB_HOST = os.getenv('WB_HOST')
WB_PASSWORD = os.getenv('WB_PASSWORD')
WB_USERNAME = os.getenv('WB_USERNAME')


def validate_data(data):
    if len(data) == 0:
        return 'LENGTH=0'
    if len(data['indicator']) == 0:
        return 'NOINDICATORS'
    return 'OKAY'


def get_bank_connection():
    try:
        conn = conn = psycopg2.connect(
            f"dbname={WB_DBNAME} user={WB_USERNAME} host={WB_HOST} port = 5432 password={WB_PASSWORD}")
        return conn
    except:
        return False


def query_bank_db(query, params=()):
    conn = get_bank_connection()
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
        cursor.execute(query, params)
        data = cursor.fetchall()
    return data


@app.route('/search', methods=['GET', 'POST'])
# TODO: Remove GET method
#  FIX assignment of variables e.g. where to tuple, for how many countries etc.
#   Figure out what kind of format JSON will be.
def search():
    error_handler = {'OKAY': '', 'NOINDICATORS': 'Please select an indicator',
                     'LENGTH=0': 'Please select countries and indicator(s)'}
    if request.method == 'GET':
        data = request.json
        conn = get_bank_connection()
        query = "SELECT value,year fROM public.indicators WHERE countrycode IN ('ARB','GBR') AND indicatorcode='EN.ATM.CO2E.GF.ZS';"
        data = query_bank_db(query)
        conn.close()

        return jsonify(data)
    if request.method == 'POST':
        search = request.get_json()
        print(search)
        error_messsage = validate_data(search)
        print(search['country'])
        # Handling 1 country:
        query_1 = "SELECT countryname,value,year FROM public.indicators WHERE countryname IN (%s) AND indicatorname IN (%s)"
        param_1_c = "Albania"
        params = tuple(
            [param_1_c, "Merchandise imports from developing economies in South Asia (% of total merchandise imports)"])
        print(params)

        db_results = query_bank_db(query_1, params)
        print(db_results)

        return jsonify(db_results)


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
