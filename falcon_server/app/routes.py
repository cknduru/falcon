from app import app
from flask import jsonify, request

@app.route('/', methods=['GET', 'POST'])
def node_info():
	if request.method == 'GET':
		return jsonify(device_name='pi', location='center console')
	elif request.method == 'POST':
		return jsonify(device_name='pi', location='center console')
