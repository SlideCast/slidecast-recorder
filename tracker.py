import mouse, time, keyboard, pickle 

def start_tracking(config):
	while config.run:
		time.sleep(0.1)
		position = mouse.get_position()

		config.mouse_points.append((config.get_time(), position))

		print ("Mouse Coordinates : " , (config.get_time(), position))

	config.save()

def end_tracking(config, event):
	config.run = False 
	config.continue_recording = False

def previous_slide(config, event):
	config.keyboard_points.append((config.get_time(), 'LEFT'))
	print ("Keyboard Event: PREVIOUS SLIDE")

def next_slide(config, event):
	config.keyboard_points.append((config.get_time(), 'RIGHT'))
	print ("Keyboard Event: NEXT SLIDE")


