from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    is_complete = db.Column(db.Boolean, nullable=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="tasks")    
    

    def to_dict(self):
        task_as_dict = {"id": self.id, "title": self.title, "is_complete": self.is_complete, "user": self.user.username}

        return task_as_dict

    @classmethod
    def from_dict(cls, task_data):
        new_task = cls(title=task_data["title"], user_id=task_data["user_id"])

        return new_task



