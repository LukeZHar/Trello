from init import db, ma

class card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    status = db.Column(db.String)
    priority = db.Column(db.String)
    date = db.Column(db.Date) # create a date 

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='cards')

class CardSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['id', 'name', 'email'])

    class Meta:
        fields = ('id', 'title', 'description', 'status', 'priority', 'date', 'user_id')


card_schema = CardSchema()
cards_schema = CardSchema(many=True)

