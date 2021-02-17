from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import json

app = Flask(__name__)
api = Api(app)

with open('country_tests_done.json') as json_file:
    json_data = json.load(json_file)

with open('date_tests_done.json') as json_file:
    json_date_data = json.load(json_file)


class Country(Resource):
    def get(self):
        # GET request
        body = request.get_json()  # obtener el request body de la solicitud
        if body is None:
            return "The request body is null", 400
        if 'country' not in body:
            return 'Specify country', 400

        country = body["country"]
        output_dict = [x for x in json_data if x['country_code'] == country]
        if not output_dict:
            return 'The country is not listed', 400
        else:
            return output_dict


class Date(Resource):
    def get(self):
        # GET request
        body = request.get_json()  # obtener el request body de la solicitud
        if body is None:
            return "The request body is null", 400
        if 'date' not in body:
            return 'Specify date', 400

        date = body["date"]
        output_dict = [x for x in json_date_data if x['date'] == date]
        if not output_dict:
            return 'The date is not listed', 400
        else:
            return output_dict


api.add_resource(Country, "/country_tests_done")
api.add_resource(Date, "/date_tests_done")

if __name__ == "__main__":
    app.run(debug=True)
