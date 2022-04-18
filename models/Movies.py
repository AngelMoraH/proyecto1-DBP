from configuration import db
class Movie(db.Model):
    __tablename__="movies"
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(),nullable=False)
    imagenURL = db.Column(db.String(),nullable=False)
    añoEstreno = db.Column(db.Integer,nullable=False)
    director = db.Column(db.String(),nullable=False)
    dateCreated =db.Column(db.DateTime,nullable=False)
    def __repr__(self):
        return f"<Movie id={self.id}, nombre={self.nombre},imagenURL={self.imagenURL},añoEstreno={self.añoEstreno},director={self.director}, dateCreated={self.dateCreated}>"

    def toJson(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "imagenURL": self.imagenURL,
            "añoEstreno": self.añoEstreno,
            "director":self.director,
            "dateCreated": self.dateCreated,
        }
