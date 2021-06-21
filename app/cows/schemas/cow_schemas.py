from marshmallow import Schema, fields, validate


class LocationSchema(Schema):
    collarId = fields.Float(required=True, default=123.45)
    cowNumber = fields.Float(required=True, default=123.45)


class CowSchema(Schema):
    id = fields.Str(required=True, example="xxxxxx-xxxx-xxxx-xxxxx")
    collarId = fields.String(required=True, example="50",
                             validate=validate.OneOf([str(i) for i in range(1, 51)]),
                             error_messages={"required": {"message": "Between 1 and 50 (inclusive) only", "code": 404}}
                             )
    cowNumber = fields.String(required=True, example="123")
    collarStatus = fields.String(required=True, example="123")
    lastLocation = fields.Nested(LocationSchema(), required=True)


class CowRequestSchema(Schema):
    collarId = fields.String(required=True, example="123")
    cowNumber = fields.String(required=True, example="123")
