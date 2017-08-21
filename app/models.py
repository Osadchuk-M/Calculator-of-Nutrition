from . import db


class Food(db.Model):
    __tablename__ = 'foods'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    protein = db.Column(db.Float)
    fat = db.Column(db.Float)
    carbohydrate = db.Column(db.Float)
    calories = db.Column(db.Float)
    type_of_food = db.Column(db.String(64))

    def __repr__(self):
        return '<Food %s>' % self.name
