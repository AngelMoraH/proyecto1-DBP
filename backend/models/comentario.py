from configuration import db
from models.User import like_user_comentario


class Comentario(db.Model):
    __tablename__ = "comentario"
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.JSON, nullable=False)
    ilikes = db.relationship("User", secondary=like_user_comentario, back_populates="gustar", lazy=True)
    
    def __repr__(self):
        return str({"id": self.id, "data": self.data})

    def toJson(self):
        return {"id": self.id, "data": self.data}


class ComentarioPadre(db.Model):
    __tablename__ = "comentarioPadre"
    id = db.Column(db.Integer, primary_key=True)
    comentarioId = db.Column(db.Integer, db.ForeignKey('comentario.id'), nullable=False)
    ComentarioHijo = db.relationship("ComentarioHijo", backref="ComentarioPadre", lazy=True)


class ComentarioHijo(db.Model):
    __tablename__ = "comentarioHijo"
    id = db.Column(db.Integer, primary_key=True)
    comentarioId = db.Column(db.Integer, db.ForeignKey('comentario.id'), nullable=False)
    comentarioPadreId = db.Column(db.Integer, db.ForeignKey('comentarioPadre.id'), nullable=False)
