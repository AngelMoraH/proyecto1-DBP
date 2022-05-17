import requests

url="http://127.0.0.1:5000"

def test_get_user():
    r = requests.get(url+"/getUser/1")
    assert r.status_code == 200

def test_get_user_error():
    r = requests.get(url+"/getUser/100")
    assert r.status_code == 200
    
def test_register():
    r = requests.post(url+"/register", json={"userName":"test","email":"test@tes.com", "password":"test"})
    assert r.status_code == 200

def test_register_error():
    r = requests.post(url+"/register", json={"userName":"test", "email":"test@test.com", "password":"asdasdasdasdasd"})
    assert r.status_code == 200
def test_login():
    r = requests.post(url+"/login/", json={"email":"test@tes.com", "password":"test"})
    assert r.status_code == 200
    
