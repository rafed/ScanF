from app import app, api
from flask import send_from_directory

@app.route('/')
@app.route('/index')
def serve_index():
    return send_from_directory('client/', 'index.html')

@app.route('/<path:path>')
def serve_files(path):
    return send_from_directory('client', path)
