from marshmallow import Schema,fields,validate,validates,ValidationError

class ProductSchema(Schema):
    name=fields.String()
    @validates("name")
    def validate_name(self,value):
        if not value.strip() and value[0]!="r*[A-Z]":
            raise ValidationError("Name must not be empty and must start with a capital letter")
