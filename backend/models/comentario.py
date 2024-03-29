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


