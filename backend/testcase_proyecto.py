from re import I
import unittest
from server import create_app
from configuration import setup_db
from models import Movies
import json


class TestCaseProyecto(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "practica"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            "postgres", "dev123", "localhost:5432", self.database_name
        )
        setup_db(self.app, self.database_path)

        self.new_movie = {
            "nombre": "title",
            "imagenURL": "https://www.themoviedb.org/t/p/original/wZiF79hbhLK1U2Pj9bF67NAKXQR.jpg",
            "fechaEstreno": "2022-04-21",
            "description": "A virus.",
            "calificacion": "vote_average",
            "dateCreated": "2022-05-05 09:24",
        }
        self.new_comentario = {
            "comentario": 'nuevo comentario',
            "idUser": 4,
            "idMovie": 1
        }

    # MOVIES
    def test_get_movies_success(self):
        res = self.client().get("/movies")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_movies"])
        self.assertTrue(len(data["movies"]))

    def test_get_movies_failed(self):
        res = self.client().get("/movies?page=1000")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_get_movies_by_id_success(self):
        res = self.client().get("/movies/1")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertTrue(len(data["movie"]))

    def test_get_movies_by_id_failed(self):
        res = self.client().get("/movies/1000")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "resource not found")

    def test_add_movies_success(self):
        res = self.client().post("/movies", json={"data": self.new_movie})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["movie"]))

    def test_add_movies_failed(self):
        res = self.client().post("/movies", json={})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "Unprocessable")

    def test_update_movies_success(self):
        res = self.client().put("/movies/41", json={"data": self.new_movie})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertEqual(data["message"], "pelicula actualizada con exito")
        self.assertEqual(data["movie_id"], 41)

    def test_update_movies_failed(self):
        res = self.client().put("/movies/41", json={})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "Unprocessable")

    def test_delete_movies_success(self):
        res0 = self.client().post("/movies", json={"data": self.new_movie})
        data0 = json.loads(res0.data)
        movie_id = data0["movie"]["id"]
        res = self.client().delete("/movies/{}".format(movie_id))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertTrue(data["total_movies"])

    def test_delete_movies_failed(self):
        res = self.client().delete("/movies/1000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "resource not found")

    # COMENTARIO
    def test_get_comentarios_success(self):
        res = self.client().get("/comentarios/1")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertTrue(data["total_comentarios"])
        self.assertTrue(len(data["comentarios"]))
        pass

    def test_get_comentarios_failed(self):
        res = self.client().get("/comentarios/1000")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_create_comentarios_success(self):
        res = self.client().post("/comentarios", json={"data": self.new_comentario})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertTrue(len(data["comentario"]))
        self.assertTrue(data["total_comentarios"])
    def test_create_comentarios_failed(self):
        res=self.client().post("/comentarios", json={})
        data=json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "Unprocessable")
    
    def test_update_comentarios_success(self):
        res0= self.client().post("/comentarios", json={"data": self.new_comentario})
        data0=json.loads(res0.data)
        comentario_id=data0["comentario_id"]
        res=self.client().put("/comentarios/"+str(comentario_id), json={"data":{"comentario": 'nuevo comentario 2',"idUser": 4,"idMovie": 1}})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertEqual(data["message"], "Comentario actualizado con exito")
        self.assertEqual(data["id"], comentario_id)
    def test_update_comentarios_failed(self):
        res = self.client().put("/comentarios/200", json={"data": self.new_comentario})
        data=json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "resource not found")
    def test_delete_comentarios_success(self):
        res0 = self.client().post("/comentarios", json={"data": self.new_comentario})
        data0=json.loads(res0.data)
        comentario_id=data0["comentario_id"]
        res = self.client().delete("/comentarios/"+str(comentario_id)+"/4")
        data=json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["deleted"],comentario_id)
        self.assertTrue(data["success"])
        self.assertTrue(data["total_comentarios"])
    def test_delete_comentarios_failed(self):
        res = self.client().delete("/comentarios/1000/4")
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "resource not found")
    def tearDown(self):
        pass
