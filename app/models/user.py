from app import db

class User(db.Model):
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        username = db.Column(db.String(25), nullable=False, unique=True)
        tasks = db.relationship("Task", back_populates="user", lazy=True)


