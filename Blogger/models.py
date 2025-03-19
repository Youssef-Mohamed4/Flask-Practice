from Blogger import db 

class Task(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title=db.Column(db.String(255),nullable=False)
    completed=db.Column(db.Boolean,nullable=False)