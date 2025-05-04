from ToDo import app, db, loginManager
from flask_login import UserMixin

@loginManager.user_loader
def load_user(userId):
    return User.query.get(int(userId))

class Task(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title=db.Column(db.String(255),nullable=False)
    completed=db.Column(db.Boolean,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Task ( {self.title})"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(25),nullable=False)
    email= db.Column(db.String(50),unique=True,nullable=False)
    phone=db.Column(db.String(11),unique=True,nullable=False)
    password_hash= db.Column(db.String(100),nullable=False)
    tasks= db.relationship("Task",backref="author",lazy=True)
    
    def __repr__(self):
        return f"User ( {self.name}, {self.email})"
    
with app.app_context():
    db.create_all()