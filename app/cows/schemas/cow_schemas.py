from marshmallow import Schema, fields, validate


class LocationSchema(Schema):
    long = fields.Float(required=True, example=123.45)
    lat = fields.Float(required=True, example=123.45)


class CowSchema(Schema):
    id = fields.String(required=True, example="xxxxxx-xxxx-xxxx-xxxxx")
    collarId = fields.String(required=True, example="50",
                             validate=validate.OneOf([str(i) for i in range(1, 51)]))
    cowNumber = fields.String(required=True, example="123")
    collarStatus = fields.String(required=True, example="123")
    lastLocation = fields.Nested(LocationSchema(), required=True)


class CowRequestSchema(Schema):
    collarId = fields.String(required=True, example="23",
                             validate=validate.OneOf([str(i) for i in range(1, 51)]))
    cowNumber = fields.String(required=True, example="123")
