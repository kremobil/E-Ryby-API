from db import db

class ImageModel(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)
    fish_id = db.Column(db.Integer, db.ForeignKey('fishes.id'))
    fish = db.relationship('Fishes_Model')

    def __init__(self, data, filename, fish_id):
        self.data = data
        self.filename = filename
        self.fish_id = fish_id

    def json(self):
        return {'filename': self.filename, 'fish_id': self.fish_id}
    @classmethod
    def find_by_name(cls, filename):
        return cls.query.filter_by(filename = filename).first()

    @classmethod
    def find_by_fishid(cls, id):
        return cls.query.filter_by(fish_id = id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def del_from_db(self):
        db.session.delete(self)
        db.session.commit()
