from app import db


class Vyvarovna(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    foods = db.relationship('Meal', backref='vyvarovna', lazy='dynamic')

    def __repr__(self):
        return '<Vyvarovna %r>' % (self.name)


tags = db.Table('tags',
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
                db.Column('meal_id', db.Integer, db.ForeignKey('meal.id')))


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    vyvarovna_id = db.Column(db.Integer, db.ForeignKey('vyvarovna.id'))
    tags = db.relationship('Tag', secondary=tags,
                           backref=db.backref('meals', lazy='dynamic'))

    def __repr__(self):
        return '<Meal %r>' % (self.name)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))

    def __repr__(self):
        return '<Tag %r>' % (self.title)
