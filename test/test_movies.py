import requests
url = "http://127.0.0.1:5000"

def test_get_movies():
    r = requests.get(url + "/movies/")
    assert r.status_code==200
    
def test_get_movie_id():
    r = requests.get(url + "/movies/23")
    assert r.status_code==200
    
def test_get_movie_id_error():
    r = requests.get(url + "/movies/2")
    assert r.status_code==200

def test_add_movie():
    data = {"data":{
            "nombre": "Virus:34",
            "imagenURL": "https://www.themoviedb.org/t/p/original/wZiF79hbhLK1U2Pj9bF67NAKXQR.jpg",
            "fechaEstreno": "2021-04-21",
            "description": "rus is unleashed and a chilling massacre runs through the streets of Montevideo.",
            "calificacion": 6.8,
            "dateCreated": "2023-05-05 09:24"
    }}
    r = requests.post(url + "/movies/", json=data)
    assert r.status_code==200

def test_update_movie():
    data = {"data":{
            "nombre": "Virus:3678",
            "imagenURL": "https://www.themoviedb.org/t/p/original/wZiF79hbhLK1U2Pj9bF67NAKXQR.jpg",
            "fechaEstreno": "2022-05-10",
            "description": " runs through the streets of Montevideo.",
            "calificacion": 6.8,
            "dateCreated": "2023-05-05 09:24"
    }}
    r = requests.put(url + "/movies/48", json=data)
    assert r.status_code==200

def test_delete_movie():
    r = requests.delete(url + "/movies/48")
    assert r.status_code==200

def test_delete_movie_error():
    r = requests.delete(url + "/movies/88")
    assert r.status_code==200