from app import app
from flask import jsonify, request
import subprocess

def run_sys_cmd(cmd):
	subprocess.check_output(cmd.split())

@app.route('/', methods=['GET', 'POST'])
def node_info():
	if request.method == 'GET':
		welcome_message = 'You are now connected to Falcon'
		subprocess.Popen(['bash', 'app/speak.sh', welcome_message])
		return jsonify(device_name='pi', location='center console')
	elif request.method == 'POST':
		run_sys_cmd('omxplayer app/song.mp3')
		print('playing')
		return jsonify(device_name='pi', location='center console')
