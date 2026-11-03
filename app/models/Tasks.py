from app import db
from datetime import datetime, timezone

class Task(db.Model):
    __tablename__='tasks'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    title=db.Column(db.String(100),nullable=False)
    description=db.Column(db.Text,nullable=True)
    status=db.Column(db.String(20),nullable=False,default="pending")
    due_date=db.Column(db.DateTime(timezone=True),nullable=True)
    created_at=db.Column(db.DateTime(timezone=True),default=datetime.now(timezone.utc))
    priority=db.Column(db.String(20),nullable=False,default="medium")
    updated_at=db.Column(db.DateTime(timezone=True),onupdate=datetime.now(timezone.utc))

    # Foreign field
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    category_id=db.Column(db.Integer,db.ForeignKey('categories.id'),nullable=True)

    def __repr__(self):
        return f"<Task {self.title}>"