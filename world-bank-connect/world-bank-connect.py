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


def get_bank_connection():

    try:
        conn = conn = psycopg2.connect(
            f"dbname={WB_DBNAME} user={WB_USERNAME} host={WB_HOST} port = 5432 password={WB_PASSWORD}")
        return conn
    except:
        return False


@app.route('/', methods=['GET'])  # POST
def main():
    if request.method == 'GET':
        data = request.data
        conn = get_bank_connection()
        query = "SELECT * fROM public.indicators WHERE countrycode IN ('ARB','GBR') AND indicatorcode='EN.ATM.CO2E.GF.ZS';"
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
        conn.close()

        return jsonify(data)


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
