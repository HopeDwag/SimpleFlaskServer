import csv
import json

from flask import request

from SimpleFlaskServer.FlaskServerProject.main.constants import ALLOWED_EXTENSIONS


def csv_to_json(csv_file_path):
    json_array = []
    # read csv file
    with open(csv_file_path, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csv_reader = csv.DictReader(csvf)
        # convert each csv row into python dict
        for row in csv_reader:
            # add this python dict to json array
            json_array.append(row)

    # convert python json_array to JSON String
    json_string = json.dumps(json_array, indent=4)
    return json_string


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('The Server is not running so I cant shut it down :)')
    func()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
