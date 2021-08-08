import unittest

from SimpleFlaskServer.FlaskServerProject.main.FlaskServer import app


class MyTestCase(unittest.TestCase):
    def test_homepage(self):
        test_client = app.test_client()
        response = test_client.get('/')
        assert response.status_code == 200
        assert response.get_data() == b'<h1>Richards Flask Server</h1>\n<p>A prototype flask server with a corresponding REST Client</p>'

    def test_healthcheck(self):
        test_client = app.test_client()
        response = test_client.get('/healthcheck')
        assert response.status_code == 200
        assert response.get_json()['delay in seconds'] == 0


if __name__ == '__main__':
    unittest.main()
