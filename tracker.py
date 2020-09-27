import mouse, time, keyboard, pickle 
from threading import Thread 

def start_tracking(config, debugger=print):
	count = 0
	while config.run:
		time.sleep(0.1)
		position = mouse.get_position()

		config.mouse_points.append((config.get_time(), position))
		count += 1
		if count == 12:
			debugger("Mouse Coordinates : " + str((config.get_time(), position)))
			count = 0

	config.save()

def end_tracking(config, event, debugger=print):
	config.run = False 
	config.continue_recording = False

def end_gui(config):
	config.run = False 
	config.continue_recording = False

def previous_slide(config, event, debugger=print):
	config.keyboard_points.append((config.get_time(), 'LEFT'))
	debugger("Keyboard Event: PREVIOUS SLIDE")

def next_slide(config, event, debugger=print):
	config.keyboard_points.append((config.get_time(), 'RIGHT'))
	debugger("Keyboard Event: NEXT SLIDE")


