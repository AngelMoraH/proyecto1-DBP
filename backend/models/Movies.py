from configuration import db
class Movie(db.Model):
    __tablename__="movies"
    id = db.Column(db.Integer,primary_key=True)
    data = db.Column(db.JSON,nullable=False)
    def __repr__(self):
        return str({'id': self.id,'data':self.data})
    
    def toJson(self):
        return {'id': self.id,'data':self.data}