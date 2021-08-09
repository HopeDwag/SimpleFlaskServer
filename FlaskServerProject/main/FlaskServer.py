import os
from time import sleep

from flask import Flask, request, send_from_directory, jsonify
from werkzeug.utils import secure_filename

from SimpleFlaskServer.FlaskServerProject.main import FlaskServerHelper
from SimpleFlaskServer.FlaskServerProject.main.FlaskServerHelper import shutdown_server, allowed_file
from SimpleFlaskServer.FlaskServerProject.main.constants import UPLOAD_FOLDER, VERSION, HEALTH_DELAY

# Initial Server Config
app = Flask(__name__)
# limit size for uploaded files to 16 MB max
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# In this section the endpoints of the server are defined
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Richards Flask Server</h1>
<p>A prototype flask server with a corresponding REST Client</p>'''


# TODO: can we look into what this does
@app.route('/upload', methods=['POST'])
def upload_file():
    print('saving uploaded file..')
    if 'file' not in request.files:
        return jsonify("Please give me a file")
    file = request.files['file']
    print('filename: {}'.format(file.filename))
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        path_and_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path_and_filename)
        print('saved uploaded file.')
        return jsonify(path_and_filename)


@app.route("/healthcheck")
def health():
    """Endpoint to return fabricated server health data"""
    health_status = {"healthy": True, "version": VERSION, "delay in seconds": HEALTH_DELAY}
    sleep(HEALTH_DELAY)  # wait this long in seconds
    return jsonify(health_status)


@app.route("/uploads/<path:name>")
def download_file(name):
    """Endpoint to return an uploaded CSV file"""
    return send_from_directory(
        app.config['UPLOAD_FOLDER'], name, as_attachment=True
    )


@app.route("/return_csv_as_json/<path:filename>", methods=['GET'])
def return_csv_as_json(filename):
    """Endpoint to return the a stored CSV file as JSON"""
    csv_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return FlaskServerHelper.csv_to_json(csv_file_path)


@app.route("/delete/<path:filename>", methods=['DELETE'])
def delete(filename):
    """Endpoint to delete a file off the server."""
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return "{} Deleted".format(filename)


@app.route("/files", methods=['GET'])
def list_files():
    """Endpoint to list files on the server."""
    files = []
    for filename in os.listdir(UPLOAD_FOLDER):
        path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)


@app.route('/shutdown', methods=['GET'])
def shutdown():
    """Endpoint to shutdown the server."""
    shutdown_server()
    return jsonify('Server shutting down...')


if __name__ == '__main__':
    app.run(debug=True)
