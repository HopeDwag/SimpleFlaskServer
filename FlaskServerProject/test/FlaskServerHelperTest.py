import json
import unittest

from SimpleFlaskServer.FlaskServerProject.main import FlaskServerHelper


class FlaskServerHelperTest(unittest.TestCase):

    def testCsvToJson(self):
        f = open("test_data/exampleJSON.json")
        json_data = json.load(f)
        converted_csv_data_as_json_string = FlaskServerHelper.csv_to_json("test_data/exampleCSV.csv")
        converted_csv_data_as_json_object = json.loads(converted_csv_data_as_json_string)
        self.assertEqual(converted_csv_data_as_json_object, json_data)


if __name__ == '__main__':
    unittest.main()
