from server import getting_user
import requests
import json
import jsonpath
from flask import jsonify, make_response
from UserAccounts.connections import db_select, get_db_user_connection
import psycopg2
import psycopg2.extras
from world_bank_connect.worldbank_connect import get_bank_connection

from flask import Flask, current_app

app = Flask(__name__)
with app.app_context():
    # within this block, current_app points to app.
    print (current_app.name)


baseUrl = "http://127.0.0.1:5000"
conns = get_db_user_connection()
connW = get_bank_connection()

def test_search_valid_input():
    with app.app_context(): 
        data=json.dumps({'country': ['Afghanistan', 'Albania'], 'indicator': [
                        'Merchandise imports from developing economies in South Asia (% of total merchandise imports)'], 'range': ['1964', '2020']})
        print(data)
        path = "/search"
        response = requests.post(url=baseUrl+path, headers={"Content-type": "application/json"},json= data)
        responseJson = response
        print(responseJson)
        assert response.status_code == 200
        assert responseJson == 'None'

def test_search_no_country_entered():
    with app.app_context(): 
        data=json.dumps({'country': [], 'indicator': [
                      'Merchandise imports from developing economies in South Asia (% of total merchandise imports)'], 'range': ['1964', '2020']})
        print(data)
        path = "/search"
        response = requests.post(url=baseUrl+path, headers={"Content-type": "application/json"},json= data)
        responseJson = response
        print(responseJson)
        assert response.status_code == 200
        assert responseJson == 'No Country'

def test_search_error_checking_invalid_country():
    with app.app_context(): 
        data=json.dumps({'country': 'Afghanistan', 'indicator': [
                      'Merchandise imports from developing economies in South Asia (% of total merchandise imports)'], 'range': ['1964', '2020']})
        print(data)
        path = "/search"
        response = requests.post(url=baseUrl+path, headers={"Content-type": "application/json"},json= data)
        responseJson = response
        print(responseJson)
        assert response.status_code == 200
        assert responseJson == 'NOTARRAY: country'

def test_search_error_checking_invalid_indicator():
    with app.app_context(): 
        data=json.dumps({'country': ['Afghanistan', 'Albania'], 'indicator': 
                      'Merchandise imports from developing economies in South Asia (% of total merchandise imports)', 'range': ['1964', '2020']})
        print(data)
        path = "/search"
        response = requests.post(url=baseUrl+path, headers={"Content-type": "application/json"},json= data)
        responseJson = response
        print(responseJson)
        assert response.status_code == 200
        assert responseJson == 'NOTARRAY: indicator'

def test_checking_general_output():
    with app.app_context(): 
        general_country_output = db_select(connW, "SELECT tablename from public.countries")
        general_indicators_output = db_select(connW, "SELECT indicatorname from public.series")

        path = "/general"
        response = requests.get(url=baseUrl+path)
        responseJson = json.loads(response.text)
        print(responseJson)
        assert response.status_code == 200
        assert len(responseJson[0]) == 247 ## 247 1345
        assert len(responseJson[1]) == 1345
        assert responseJson[0] == general_country_output
        assert responseJson[1] == general_indicators_output

def test_get_user_post():
    data = [{"name": "mike",
"password":"test2"}]
    path = "/get_user"
    response = requests.post(url=baseUrl+path, headers={"Content-type": "application/json"},json= data)
    responseJson = json.loads(response.text)
    print(responseJson)
    assert responseJson ==  [
    {
        "id": 10,
        "password": "$2b$12$4OTGs89gtH7aJzXpk5/HXev5pBk1xKy3Dhk94zj7Og1FO6WdfM0yG",
        "salt": "$2b$12$4OTGs89gtH7aJzXpk5/HXe",
        "type_id": 1,
        "username": "mike"
    }
]

def test_get_user_no_user_found():
    data = [{"name": "missingName",
"password":"test4"}]
    path = "/get_user"
    response = requests.post(url=baseUrl+path, headers={"Content-type": "application/json"},json= data)
    responseJson = json.loads(response.text)
    assert responseJson ==  [{'message': 'user was not found', 'status': 404}]


def test_create_user():
    user = "mike_test_api"
    db_select(conns, 'delete from user_table where username = %s returning id', ((user),))
    data = [{"name": 'mike_test_api',"password":'test2'}]
    path = "/create_user"
    response = requests.post(url=baseUrl+path, headers={"Content-type": "application/json"},json= data)
    responseJson = json.loads(response.text)
    find_user = db_select(conns, 'select from user_table where username = %s', ((user),))
    assert response.status_code == 200
    assert responseJson[0]['message'] == 'user created'
    # assert responseJson == find_user

def test_create_user_already_in():
    user = "mike_test_api"
    data = [{"name": 'mike_test_api',"password":'test2'}]
    path = "/create_user"
    response = requests.post(url=baseUrl+path, headers={"Content-type": "application/json"},json= data)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert responseJson[0]['message'] == 'user is already in database'

def test_get_user() :
    with app.app_context():    
        allusers = db_select(conns, 'select * from user_table')
        path = "/get_user"
        response = requests.get(url=baseUrl+path)
        responseJson = json.loads(response.text)
        assert response.status_code == 200
        assert responseJson == allusers
        
