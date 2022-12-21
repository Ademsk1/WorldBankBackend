from server import getting_user
import requests
import json
import jsonpath

baseUrl = "http://127.0.0.1:5000"
    

def test_get_user_post():
    data = [{"name": "mike",
"password":"test2"}]
    path = "/get_user"
    response = requests.post(url=baseUrl+path, headers={"Content-type": "application/json"},json= data)
    responseJson = json.loads(response.text)
    print(responseJson)
    assert responseJson ==     [
    {
        "id": 10,
        "password": "$2b$12$4OTGs89gtH7aJzXpk5/HXev5pBk1xKy3Dhk94zj7Og1FO6WdfM0yG",
        "salt": "$2b$12$4OTGs89gtH7aJzXpk5/HXe",
        "type_id": 1,
        "username": "mike"
    }
]

def create_user_test():
    data = [{"name": 'mike',"password":'test2'}]

def test_get_user() :
    path = "/get_user"
    response = requests.get(url=baseUrl+path)
    responseJson = json.loads(response.text)
    print(responseJson)
    assert response.status_code == 200

    assert responseJson == [
    {
        "id": 1,
        "password": "$2b$12$eophcZFok2WsQnByTEbFT.N.0C23n5QcCZfiVjYCdxc/dUz8cJFVS",
        "salt": "$2b$12$eophcZFok2WsQnByTEbFT.",
        "type_id": 1,
        "username": "mike"
    },
    {
        "id": 2,
        "password": "$2b$12$b.BPudmUJnO4rS1U19.Qdez.AVNoCNAc1fzxbx0m9cCF8DaGUg5ce",
        "salt": "$2b$12$b.BPudmUJnO4rS1U19.Qde",
        "type_id": 1,
        "username": "cal"
    },
    {
        "id": 3,
        "password": "$2b$12$aAqCfxB19IXzNRqQj7Cbpe/JFjshWWuPbN4/qpDb3o/h.Qz.ODh4K",
        "salt": "$2b$12$aAqCfxB19IXzNRqQj7Cbpe",
        "type_id": 1,
        "username": ""
    },
    {
        "id": 4,
        "password": "$2b$12$lEf8x0fyBG3ajQEgvxfKaOZ6ytFI0m/hs/sxRjjGE1HV080EVudyu",
        "salt": "$2b$12$lEf8x0fyBG3ajQEgvxfKaO",
        "type_id": 1,
        "username": "callumhall"
    },
    {
        "id": 5,
        "password": "$2b$12$TVoWz3qhtP7ttHa3qaPhLOS9z9Hrrd3ywLpqzJsoldq3iKELyJdY.",
        "salt": "$2b$12$TVoWz3qhtP7ttHa3qaPhLO",
        "type_id": 1,
        "username": "mike"
    },
    {
        "id": 6,
        "password": "$2b$12$C0WF2GEbcQ6iHkRfUtQp9.BBQoKuTzSaQB0nSu.vfh8cX1Pc2YHze",
        "salt": "$2b$12$C0WF2GEbcQ6iHkRfUtQp9.",
        "type_id": 1,
        "username": "cal"
    },
    {
        "id": 7,
        "password": "$2b$12$bcQ4vvvW38MB.wh3OY3QbOE1NDfeagKGjvfip5ktOr.jIOVvior7O",
        "salt": "$2b$12$bcQ4vvvW38MB.wh3OY3QbO",
        "type_id": 1,
        "username": "Will"
    },
    {
        "id": 8,
        "password": "$2b$12$DQZK2q9as5qXyOeuB2WUauII6hEJrgxb2FNroM9h54HVzABdOkCQG",
        "salt": "$2b$12$DQZK2q9as5qXyOeuB2WUau",
        "type_id": 1,
        "username": "Will"
    },
    {
        "id": 9,
        "password": "$2b$12$nLyanMVwJnxoqj/uf/UBv.4IHW2iFkl5h4WRYXcUGpOOzZ9WqYu2q",
        "salt": "$2b$12$nLyanMVwJnxoqj/uf/UBv.",
        "type_id": 1,
        "username": "{mike,test}"
    },
    {
        "id": 10,
        "password": "$2b$12$4OTGs89gtH7aJzXpk5/HXev5pBk1xKy3Dhk94zj7Og1FO6WdfM0yG",
        "salt": "$2b$12$4OTGs89gtH7aJzXpk5/HXe",
        "type_id": 1,
        "username": "mike"
    }
]