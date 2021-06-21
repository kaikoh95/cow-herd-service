import uuid

from app.cows.models.cow import Cow
from app.cows.models.services import HalterCowApi
from app.helpers.common_helpers import convert_to_snake_case
from app.helpers.exceptions_handlers import exception_handler


class CowCommonHelpers:
    def __init__(self):
        self.client = HalterCowApi()

    @staticmethod
    def get_all_cows():
        return [cow.serialize() for cow in Cow.query.all()]

    def construct_cow(self, **kwargs):
        """Creates a Cow object from given details"""
        cow_status = self.latest_halter_cow_status(collar_id=kwargs.get("collar_id"))
        cow_data = self.construct_cow_data(cow_status=cow_status, **kwargs)

        cow = Cow.query.filter_by(id=kwargs.get("id")).scalar() or Cow(**cow_data)
        if cow:
            for key, value in cow_data.items():
                setattr(cow, key, value)
        return cow.save()

    @staticmethod
    def construct_cow_data(cow_status, **kwargs):
        cow_data = {
            "collar_status": "Healthy" if cow_status.get("healthy", False) is True else "Broken",
            "long": float(cow_status.get("long") or cow_status.get("lng")),
            "lat": float(cow_status.get("lat")),
            "collar_id": kwargs.get("collar_id"),
            "cow_number": kwargs.get("cow_number"),
            "id": kwargs.get("id") or str(uuid.uuid4()),
        }
        return cow_data

    @exception_handler
    def latest_halter_cow_status(self, collar_id):
        """Fetches collar status and locations from Halter API"""
        cow_statuses = self.client.get_halter_cow_statuses(collar_id)
        cow_statuses = convert_to_snake_case(cow_statuses)
        cow_status = sorted(cow_statuses, key=lambda x: x["timestamp"], reverse=True)[0]

        return cow_status
