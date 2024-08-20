from init import db, ma

class User(db.Model):
    # NAme of the table
    __tablename__ = 'users'

    # Attributes of the table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin')

# To handle a single user object
user_schema = UserSchema(exclude=['password'])

# To handle a list of user objects
users_schema = UserSchema(many=True, exclude=['password'])