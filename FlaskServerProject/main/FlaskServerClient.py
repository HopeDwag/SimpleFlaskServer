import requests


class FlaskServerClient:

    def __init__(self, endpoint="http://127.0.0.1:5000", key="", secret=""):
        self.endpoint = endpoint
        # the key and secret will be used later in the implementation for security
        self.key = key
        self.secret = secret

    def get_files(self):
        path = "%s/files" % self.endpoint
        return requests.get(path, timeout=30, verify=True).json()

    def shutdown(self):
        path = "%s/shutdown" % self.endpoint
        return requests.get(path, timeout=30, verify=True).json()

    def upload_filename(self):
        path = "%s/upload" % self.endpoint
        return requests.get(path, timeout=30, verify=True).json()

    def download_filename(self, filename):
        path = "%s/uploads/%s" % self.endpoint, filename
        return requests.get(path, timeout=30, verify=True).json()

    def health_check(self):
        path = "%s/healthcheck" % self.endpoint
        return requests.get(path).json()
