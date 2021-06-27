import os
from flask import Flask, request
from flask_restful_swagger_2 import Api
from flask_cors import CORS
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin


VERSION = "v1"


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    api = Api(app)

    # Create an APISpec
    spec = APISpec(
        title="Kai Koh's Cow Herd Service",
        version=VERSION,
        openapi_version="3.0.2",
        plugins=[FlaskPlugin(), MarshmallowPlugin()],
        info={
            "description": "Contains API services built as part of Halter's assessment",
        }
    )

    # App environment config
    settings = os.getenv('SETTING', 'app.config.base.BaseConfig')
    app.config.from_object(settings)

    # REST API Resource Views
    from app.cows.views.cows_view import CowsView
    from app.cows.views.single_cow_view import SingleCowView

    cows_view = CowsView.as_view("CowsView")
    app.add_url_rule('/cows', view_func=cows_view)

    single_cow_view = SingleCowView.as_view("SingleCowView")
    app.add_url_rule('/cows/<id>', view_func=single_cow_view)

    # Register specs
    with app.test_request_context():
        spec.path(view=cows_view)
        spec.path(view=single_cow_view)

    # Register schemas
    from app.cows.schemas.cow_schemas import CowSchema, LocationSchema, CowRequestSchema

    spec.components.schema("LocationSchema", schema=LocationSchema)
    spec.components.schema("CowSchema", schema=CowSchema)
    spec.components.schema("CowRequestSchema", schema=CowRequestSchema)

    # Default routes
    @app.route('/', methods=['GET'])
    def home():
        args = request.args
        out = {
            "message": "Welcome to Kai's Cow Herd Service for Halter Assessment. "
                       f"You can view Swagger docs at /spec with a Swagger client"
        }
        if args:
            out = {**out, **args}
        return out, 200, {'Content-Type': 'application/json'}

    @app.route("/spec", methods=['GET'])
    def specs():
        openapi = {
            **spec.to_dict(),
            "servers": [
                {
                    "url": "http://localhost:5000",
                    "description": "Local",
                },
            ]
        }

        return openapi, 200

    @app.errorhandler(400)
    def bad_request(error):
        error = vars(error)
        message = "The browser (or proxy) sent a request that this server could not understand."
        if error.get("data") and error.get("data").get('error'):
            message = error["data"]["error"]
        out = {'error': message}
        return out, 400

    @app.errorhandler(404)
    def not_found(error):
        error = vars(error)
        message = "The requested URL was not found on the server."
        if error.get("data") and error.get("data").get('error'):
            message = error["data"]["error"]
        out = {'error': message}
        return out, 404

    # Api Error Handlers
    from app.config.app_error_handlers import app_error_handlers
    app_error_handlers(app)

    return app
