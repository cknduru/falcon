#!/usr/bin/python
import gpiozero as gp

initialised = False
placements = None

def setup_relay_data():
	global initialised
	global placements

	print('initialising relay data')

	# [0] is pin number [1] is relay object registered at a certian pin
	# new relay channels are added here
	# placements = {"door" : (3, None)}
	placements = {"footwell" : (2, None)}

	# initialise placements
	for placement in placements:
		gpio_pin = placements[placement][0]
		placements[placement] = (gpio_pin, gp.OutputDevice(gpio_pin, active_high=True, initial_value=False))

	initialised = True

def is_valid_placement(placement):
	try:
		placements[placement]
		return True
	except:
		print('Non-valid placement: {}'.format(placement))
		return False

def toggle_relay(placement):
	if not initialised:
		setup_relay_data()

	if is_valid_placement(placement):
		relay_container = placements[placement]
		gpio_pin = relay_container[0]
		relay_container[1].toggle()

		print('switched relay chan {} on @ {}'.format(gpio_pin, placement))
	else:
		return
