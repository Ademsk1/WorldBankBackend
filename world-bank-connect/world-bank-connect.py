from flask import Flask, jsonify, request
import os
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
pw = os.getenv('GCP_PROJECT_ID')
print(pw)
WB_DBNAME = os.getenv('WB_DBNAME')
WB_HOST = os.getenv('WB_HOST')
WB_PASSWORD = os.getenv('WB_PASSWORD')
WB_USERNAME = os.getenv('WB_USERNAME')


def get_bank_connection():

    try:
        conn = conn = psycopg2.connect(
            f"dbname={WB_DBNAME} user={WB_USERNAME} host={WB_HOST} port = 5432 password={WB_PASSWORD}")
        print('connected')
        return conn
    except:
        return False


@app.route('/', methods=['GET'])
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


if __name__ == '__main__':
    app.run(debug=True, port='5000')
