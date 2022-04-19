from configuration import db
class Likes(db.Model):
    __tablename__="likes"
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.JSON,nullable=False)
    
    def __repr__(self):
        return str({'id': self.id,'data':self.data})

    

