from app import app
from flask import jsonify, request

@app.route('/', methods=['GET', 'POST'])
def node_info():
	if request.method == 'GET':
		return jsonify(device_name='pi', location='center console')
	elif request.method == 'POST':
		import subprocess
		subprocess.check_output(['omxplayer', 'app/song.mp3'])
		print('playing')
		return jsonify(device_name='pi', location='center console')
