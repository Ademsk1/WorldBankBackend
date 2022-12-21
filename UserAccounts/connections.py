import psycopg2
import psycopg2.extras
import os
from dotenv import load_dotenv

load_dotenv()
PASS = os.getenv('PASS')
HOST = os.getenv('HOST')
USER = os.getenv('USER')

def get_db_user_connection():
    try:
        conn = psycopg2.connect(f"dbname=backvrlw user=backvrlw host=mel.db.elephantsql.com port = 5432 password={PASS}")
        return conn
    except:
        print('couldnt connect to server')

def db_select(conn ,query, parameters=()):
    if conn != None:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            # try:
                cur.execute(query, parameters)
                data = cur.fetchall()
                conn.commit()
                return data            
            # except:
            #     return "Error executing query."
    else:
        return "No connection"