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

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'priority': self.priority,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'user_id': self.user_id,
            'category_id': self.category_id
        }