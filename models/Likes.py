from configuration import db
class Likes(db.Model):
    __tablename__="likes"
    id = db.Column(db.Integer, primary_key=True)
    idMovie = db.Column(db.Integer,nullable=False)
    idUsuario = db.Column(db.Integer,nullable=False)
    boolLike = db.Column(db.Boolean,nullable=False)
    dateCreated =db.Column(db.DateTime,nullable=False)
    def __repr__(self):
        return f"<Likes id={self.id}, idMovie={self.idMovie},idUsuario={self.idUsuario},boolLike={self.boolLike}, dateCreated={self.dateCreated}>"

    def toJson(self):
        return {
            "id": self.id,
            "idMovie": self.idMovie,
            "idUsuario": self.idUsuario,
            "boolLike": self.boolLike,
            "dateCreated": self.dateCreated,
        }
    