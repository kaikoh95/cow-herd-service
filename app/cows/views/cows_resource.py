from app.cows.helpers.cow_common_helpers import CowCommonHelpers
from app.cows.schemas.cow_schemas import CowRequestSchema, CowSchema
from app.helpers.common_helpers import process_request_body
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs


class CowsResource(MethodResource):
    """Contains methods for reading/creating Cows endpoint."""

    @doc(description='Gets all Cows that are currently in the database.', tags=['Cows'])
    @marshal_with(CowSchema(many=True), description="A list of Cows.", code=200)
    def get(self, **kwargs):
        cows = CowCommonHelpers.get_all_cows()
        return CowSchema(many=True).dump(cows), 200

    @doc(description='Creates a Cow and saves it in the database.', tags=['Cows'])
    @use_kwargs(CowRequestSchema, location="json", description="Accepts unique Cow number and Collar ID strings.")
    @marshal_with(CowSchema, description="A Cow object.", code=200)
    def post(self, **kwargs):
        payload = process_request_body(schema=CowRequestSchema())
        cow = CowCommonHelpers().construct_cow(**payload).serialize()
        return CowSchema().dump(cow), 200
