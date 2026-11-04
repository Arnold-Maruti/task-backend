
from app import db
from datetime import datetime,timezone


# Users model represents the users table in the database.
# Each model normally inherits from db.Model, which is a base class for all models in Flask-SQLAlchemy.
class User(db.Model):
    __tablename__ = 'users'

    # Defining columns for the users table.
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc))    
   


    # Relationships are used to help us understand how one table relates to another.For a one to many relationship the relationship part is declared in the parent table as shown below.
    tasks=db.relationship('Task',backref='user',lazy=True,cascade="all, delete-orphan")
    categories=db.relationship('Category',backref='user',lazy=True,cascade="all, delete-orphan")


    def __repr__(self):
        return f"<User {self.username}>"

    def to_dict(self):  
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }