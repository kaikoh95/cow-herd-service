from app.helpers.exceptions_handlers import exception_handler
from app.services.halter.api import HalterCowApiWrapper


class HalterCowApi:

    def __init__(self):
        self.client = HalterCowApiWrapper()

    @staticmethod
    def __build_query_string(params):
        query = ""
        for key, value in params.items():
            query += f"{key}={value}&"
        if query[-1] == "&":
            query = query[:-1]
        return query

    def __get_response(self, path, params=None):
        if params:
            query = self.__build_query_string(params=params)
            path += f"?{query}"
        response = self.client.get(path=path)
        return response

    def get_halter_cow_statuses(self, collar_id):
        path = f"/device/{collar_id}/status"
        return self.__get_response(path=path)
