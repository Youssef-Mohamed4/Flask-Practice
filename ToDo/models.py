from ToDo import db ,loginManager

@loginManager.user_loader
def load_user(userId):
    return User.query.get(int(userId))

class Task(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title=db.Column(db.String(255),nullable=False)
    completed=db.Column(db.Boolean,nullable=False)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(25),nullable=False)
    email= db.Column(db.String(50),unique=True,nullable=False)
    phone=db.Column(db.String(11),unique=True,nullable=False)
    password_hash= db.Column(db.String(100),nullable=False)
    tasks= db.relationship("Task",backref="owner",lazy=True)