class User(UserMixin, db.Model):
#     __tablename__ = "users"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     email = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(50))
#     posts = relationship('BlogPost', back_populates='author')