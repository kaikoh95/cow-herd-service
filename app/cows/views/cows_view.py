from flask_restful import Resource
from flask import jsonify, make_response
from app.cows.helpers.cow_common_helpers import CowCommonHelpers
from app.cows.schemas.cow_schemas import CowRequestSchema
from app.helpers.common_helpers import process_request_body


class CowsView(Resource):
    """Contains methods for reading/creating Cows endpoint."""

    def get(self):
        """
        Gets all Cows
        ---
        description: Gets all Cows that are currently in the database
        responses:
            200:
                description: A list of Cows
                content:
                    application/json:
                        schema:
                            type: array
                            items:
                                $ref: "#/components/schemas/CowSchema"
            500:
                description: Internal Server Error
        """

        cows = CowCommonHelpers.get_all_cows()
        return make_response(jsonify(cows), 200)

    def post(self):
        """
        Creates a Cow
        ---
        description: Creates a Cow and saves it in the database
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
                description: Internal server error
        """

        payload = process_request_body(schema=CowRequestSchema())
        cow = CowCommonHelpers().construct_cow(**payload)
        return cow.serialize(), 200
