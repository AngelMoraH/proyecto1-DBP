import requests

url = "http://127.0.0.1:5000"


def test_getComentario():
    r = requests.get(url + "/comentario/23")
    assert r.status_code == 200


def test_addComentario():
    r = requests.post(
        url + "/comentario/",
        json={
            "data": {
                "comentario":"comentario prueba",
                "idUser":4,
                "idMovie":2,
                "dateCreated":""
            }
        },
        headers={"Content-Type": "application/json"},
    )
    assert r.status_code == 200


def test_updateComentario():
    r = requests.put(
        url + "/comentario/83",
        json={
            "data": {
                "comentario": "comentario prueba",
                "idUser":1,
                "idMovie":2,
            }
        },
        headers={"Content-Type": "application/json"},
    )
    assert r.status_code == 200

def test_updateComentario_error():
    r = requests.put(
        url + "/comentario/970",
        json={
            "data": {
                "comentario": "comentario prueba",
                "idUser":1,
                "idMovie":23,
            }
        },
        headers={"Content-Type": "application/json"},
    )
    assert r.status_code == 200


def test_deleteComentario():
    r = requests.delete(url + "/comentario/97/4")
    assert r.status_code == 200
    
def test_deleteComentario_error():
    r = requests.delete(url + "/comentario/84/2")
    assert r.status_code == 200