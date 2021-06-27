from app.cows.helpers.cow_common_helpers import CowCommonHelpers
from app.cows.schemas.cow_schemas import CowRequestSchema, CowSchema
from app.helpers.common_helpers import process_request_body
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs


class SingleCowResource(MethodResource):
    """Contains methods for reading/updating/deleting a Cow."""

    @doc(description='Updates a Cow and saves it in the database. '
                     'This creates a Cow if not already exists.',
         tags=['Cows'])
    @use_kwargs(CowRequestSchema, location="json", description="Accepts unique Cow number and Collar ID strings.")
    @marshal_with(CowSchema, description="A Cow object.", code=200)
    def put(self, **kwargs):
        payload = {
            **process_request_body(CowRequestSchema()),
            "id": kwargs.get("id")
        }
        cow = CowCommonHelpers().construct_cow(**payload).serialize()
        return CowSchema().dump(cow), 200
