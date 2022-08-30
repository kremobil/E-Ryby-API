from sqlalchemy import false

from db import db

class Fishes_Model(db.Model):
    __tablename__ = 'fishes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    latinName = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    protected = db.Column(db.Boolean, default=False)
    bait = db.Column(db.String(80), nullable=False)
    attitude = db.Column(db.String(80), default='Żeru spokojnego')

    def __init__(self, name, latinName, description, bait, attitude, protected):
        self.name = name
        self.latinName = latinName
        self.description = description
        self.bait = bait
        self.attitude = attitude
        self.protected = protected

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'latinName': self.latinName,
            'description': self.description,
            'bait': self.bait,
            'attitude': self.attitude,
            'protected': self.protected,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def del_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

