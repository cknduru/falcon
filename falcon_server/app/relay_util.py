#!/usr/bin/python
import gpiozero as gp

initialised = False
placements = None

def setup_relay_data():
	global initialised
	global placements

	placements = {"footwell" : (2, None)}

	for placement in placements:
		gpio_pin = placements[placement][0]
		placements[placement] = (gpio_pin, gp.OutputDevice(gpio_pin, active_high=False, initial_value=False))

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
		print('initialising relay data')
		setup_relay_data()

	if is_valid_placement(placement):
		relay_container = placements[placement]
		gpio_pin = relay_container[0]
		relay_container[1].toggle()
		
		print('switched relay chan {} on @ {}'.format(gpio_pin, placement))
	else:
		return