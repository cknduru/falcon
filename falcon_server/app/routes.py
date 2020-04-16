#!/usr/bin/python
from app import app
from flask import jsonify, request, make_response
import subprocess
import app.relay_util as ru
from threading import Thread
import app.time_manager as tm

cmd_q = []
time_manager_started = False

# todo: suppress output from Popen
# disable cross use of audio between threads with bool or lock file
# add 200 return code to GET response as done with POST

def run_sys_cmd(cmd):
	subprocess.Popen(cmd.split())

@app.route('/', methods=['GET', 'POST'])
def node_info():
	global cmd_q
	global time_manager_started

	if request.method == 'GET':
		welcome_message = 'You are now connected to Falcon'
		subprocess.Popen(['bash', 'app/speak.sh', welcome_message])

		if not time_manager_started:
			Thread(target=tm.setup, args=(cmd_q,)).start()
			# register static time evens
			# this should be moved
			cmd_q.append(('TIME', '21:20', 'toggleLights'))

			time_manager_started = True

		return jsonify(device_name='pi', location='center console')
	elif request.method == 'POST':
		data = request.get_json(force=True)
		cmd = data['command']

		print('command = {}'.format(cmd))

		if cmd == 'playMusic':
			run_sys_cmd('omxplayer app/song.mp3')
		elif 'toggleLights' in cmd:
			placement = cmd.split(' ')[1]
			ru.toggle_relay(placement)
		elif 'shutdown' in cmd:
			run_sys_cmd('sudo shutdown -h now')
		data = {'message': 'Created', 'code': 'SUCCESS'}
		return make_response(jsonify(data), 200)
	else:
		# invalid command
		return jsonify({'error': 'invalid command'}), 401
