from app import db
# from datetime import datetime

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    # completed_at = db.Column(db.DateTime, nullable=True)
    
    
    @classmethod
    def from_dict(cls, task_data):
        return cls(title=task_data["title"])
                        # description=task_data["description"])

    def to_dict(self):
        task_as_dict = {"id": self.task_id, "title": self.title} 
        # , "completed_at": self.completed_at}

        return task_as_dict

        # if self.goal_id:
        #     return dict(

        #     id=self.task_id, 
        #     title=self.title,
        #     is_complete=bool(self.completed_at)
        
        # )
        # else:
        #     return dict(
        #         id=self.task_id, 
        #         title=self.title,
        #         is_complete=bool(self.completed_at)
            
        #     )