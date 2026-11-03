from app import db
from datetime import datetime, timezone

class Category(db.Model):
    __tablename__='categories'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(100),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)

    tasks=db.relationship('Task',backref='category',cascade="all, delete-orphan",lazy=True)

    def __repr__(self):
        return f"<Category {self.name}>"