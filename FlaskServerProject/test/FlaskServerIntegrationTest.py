import threading
import unittest

from SimpleFlaskServer.FlaskServerProject.main import FlaskServer
from SimpleFlaskServer.FlaskServerProject.main.FlaskServerClient import FlaskServerClient

# NOTE: This integration test is under development and is currently only a collection of snippets
class FlaskServerIntegrationTest(unittest.TestCase):

    def test_flask_server_integration(self):
        self.setUp()
        # print("starting integration test")
        client = FlaskServerClient(endpoint="http://127.0.0.1:5000", key=22, secret=22)
        # response = test_client.get('/')
        # assert response.status_code == 200
        client.healthcheck()
        client.shutdown()

    def setUp(self):
        FlaskServer.app.testing = True
        FlaskServer.app.threaded = True
        t1 = threading.Thread(target=FlaskServer.app.run(debug=False, use_reloader=False)).start()
        # # logger.info(f'start second thread')
        t2 = threading.Thread(print('hello')).start()
        # self.app = FlaskServer.app.run(debug=False,use_reloader=False)
        t1.append(t2)
        t1.start()
        # t2.start()

        return self.app

    def integration_test(self):
        client = FlaskServerClient(endpoint="http://127.0.0.1:5000", key=22, secret=22)
        client.healthcheck()
        client.shutdown()
        print("hello")

    def integration_server(self):
        FlaskServer.app.run()


if __name__ == '__main__':
    unittest.main()
