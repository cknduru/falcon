from app import app
from flask import jsonify

@app.route('/')
def node_info():
    return jsonify(device_name='pi', location='center console')
