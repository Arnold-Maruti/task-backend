from marshmallow import Schema,fields,validate,validates,ValidationError,validates_schema
from datetime import datetime, timezone

class TaskSchema(Schema):
    # Auto-generated fields i.e they are only required when dumping data from the database to the client, not when loading data from the client to the database.
    id=fields.Integer(dump_only=True)
    created_at=fields.DateTime(dump_only=True)
    updated_at=fields.DateTime(dump_only=True)
    category_id=fields.Integer(dump_only=True)
    user_id=fields.Integer(dump_only=True)

    title=fields.String(required=True,validate=validate.Length(min=1, max=100))

    description=fields.String(load_default=None, validate=validate.Length(min=1) )

    status=fields.String(load_default="pending", validate=validate.OneOf(["pending", "in_progress", "completed"]))

    due_date=fields.DateTime(load_default=None)

    priority=fields.String(load_default="medium", validate=validate.OneOf(["low", "medium", "high"]))


class TaskUpdateSchema(Schema):
    title=fields.String(validate=validate.Length(min=1, max=100))
    description=fields.String(validate=validate.Length(min=1))
    status=fields.String(validate=validate.OneOf(["pending", "in_progress", "completed"]))
    due_date=fields.DateTime()
    priority=fields.String(validate=validate.OneOf(["low", "medium", "high"]))
    category_id=fields.Integer()


@validates("title")
def validate_title(self,value):
    if not value.strip():
        raise ValidationError("Title cannot be empty.") 


@validates_schema
def validate_due_date(self,data,**kwargs):
    due_date=data.get("due_date")
    if due_date and due_date < datetime.now(timezone.utc):
        raise ValidationError("Due date cannot be in the past.", field_name="due_date")  

