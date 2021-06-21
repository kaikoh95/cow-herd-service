from flask_restful import Resource
from app.cows.helpers.cow_common_helpers import CowCommonHelpers
from app.cows.schemas.cow_schemas import CowRequestSchema
from app.helpers.common_helpers import process_request_body


class SingleCowView(Resource):
    """Contains methods for reading/updating/deleting a Cow."""

    @staticmethod
    def put(**kwargs):
        """
        Updates a Cow
        ---
        description: Updates a Cow and saves it in the database. This creates a Cow if not already exists.
        parameters:
          - name: id
            in: path
            required: true
            schema:
              type: string
              example: 123
        requestBody:
            required: true
            description: Contains a Cow's Collar Id and Cow Number
            content:
                application/json:
                    schema:
                        $ref: '#/components/schemas/CowRequestSchema'
        responses:
            200:
                description: A Cow object
                content:
                    application/json:
                        schema:
                            $ref: "#/components/schemas/CowSchema"
            400:
                description: Bad Request
            404:
                description: Not Found
            500:
                description: Internal Server Error
        """
        payload = {
            **process_request_body(CowRequestSchema()),
            "id": kwargs.get("id")
        }
        cow = CowCommonHelpers().construct_cow(**payload)
        return cow.serialize(), 200
