from configuration import db

class User(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    dateCreated = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return str({"id": self.id,"userName": self.userName,"email": self.email,"password": self.password,"dateCreated": self.dateCreated})
