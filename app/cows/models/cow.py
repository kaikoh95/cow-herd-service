from datetime import datetime
from app.config.db import db
from app.helpers.common_helpers import convert_to_camel_case
from app.helpers.exceptions_handlers import exception_handler, SaveToDbError


class Cow(db.Model):
    __tablename__ = "cow"

    id = db.Column(db.String(255), primary_key=True, nullable=False)
    collar_id = db.Column(db.String(255), unique=True, nullable=False)
    cow_number = db.Column(db.String(255), unique=True, nullable=False)
    collar_status = db.Column(db.String(255), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    long = db.Column(db.Float, nullable=False)

    # audit purposes
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __init__(self, iterable=(), **kwargs):
        self.__dict__.update(iterable, **kwargs)

    def serialize(self):
        """Converts model into readable format in camel case"""
        data = {
            "id": self.id,
            "collar_id": self.collar_id,
            "cow_number": self.cow_number,
            "collar_status": self.collar_status,
            "last_location": {
                "lat": self.lat,
                "long": self.long,
            }
        }
        return convert_to_camel_case(data)

    @exception_handler
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            raise SaveToDbError(e)
        return self
