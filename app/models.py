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

    @staticmethod
    def nutrients_need(weight):
        return {
            'protein': weight * 2.5,
            'fat': weight * 1.2,
            'carbohydrate': weight * 5
        }

    @staticmethod
    def nutrients_got(products):
        products = [(Food.query.filter_by(name=product[0]).first(), float(product[1])) for product in products]
        protein = sum([product[0].protein * product[1] for product in products])
        fat = sum([product[0].fat * product[1] for product in products])
        carbohydrate = sum([product[0].carbohydrate * product[1] for product in products])
        return {
            'protein': protein,
            'fat': fat,
            'carbohydrate': carbohydrate
        }
