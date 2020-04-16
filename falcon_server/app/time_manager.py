#!/usr/bin/python
from time import sleep, strftime, localtime
import app.relay_util as ru

# format of tuple is hour:minute, cmd
time_events = list()

# should this use Python time libs instead?
def has_passed_h_m(t_time):
	current_time = strftime("%H:%M", localtime()).split(':')
	trigger_time = t_time.split(':')

	hour_c = current_time[0]
	min_c  = current_time[1]
	hour_t = trigger_time[0]
	min_t  = trigger_time[1]

	print('{}:{} - {}:{}'.format(hour_c, min_c, hour_t, min_t))

	if hour_c >= hour_t and min_c >= min_t:
		return True
	return False
	
def register_new_event(event_t):
	global time_events

	# add event tuple to events
	time_events.append(event_t)

def trigger_outstanding_events():
	global time_events

	# a copy of time_events is needed because we add and remove elements in the loop
	time_events_tmp = time_events

	for te in time_events_tmp:
		trig_time = te[0]
		cmd = te[1]

		if has_passed_h_m(trig_time):
			print('trigger of {} @ {}'.format(cmd, trig_time))
			print('before: {}'.format(time_events))
			if cmd == 'toggleLights':
				ru.toggle_relay('footwell')
				
			time_events.remove(te)
			print('after: {}'.format(time_events))

def setup(cmd_q):
	while True:
		try:
			msg = cmd_q.pop(0)
			print('time manager got message {}'.format(msg))

			trig_type = msg[0]
			trig_time = msg[1]
			trig_cmd  = msg[2]

			if trig_type == 'TIME':
				register_new_event((trig_time, trig_cmd))
		except:
			# no messages for us
			print('no msg')
			pass

		# trigger events that are ready
		trigger_outstanding_events()
		sleep(4)


