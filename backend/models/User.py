from configuration import db

like_user_comentario = db.Table('LikeUserComentario',
    db.Column('idUser', db.Integer, db.ForeignKey('usuario.id')),
    db.Column('idComentario', db.Integer, db.ForeignKey('comentario.id')))

class User(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    dateCreated = db.Column(db.DateTime, nullable=False)
    gustar = db.relationship("Comentario",secondary=like_user_comentario,back_populates="ilikes",lazy=True)
    
    
    def __repr__(self):
        return str(
            {
                "id": self.id,
                "userName": self.userName,
                "email": self.email,
                "password": self.password,
                "dateCreated": self.dateCreated
            }
        )

    def toJson(self):
        return {
            "id": self.id,
            "userName": self.userName,
            "email": self.email,
            "password": self.password,
            "dateCreated": self.dateCreated
        }

