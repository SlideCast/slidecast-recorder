from threading import Thread 
import mouse, time, keyboard, pickle 

def on_press_key_args(key, callback, config, suppress=False):
    return keyboard.hook_key(key, lambda e: e.event_type == keyboard.KEY_UP or callback(config, e), suppress=suppress)

class Config:
	def __init__(self):
		self.run = True
		self.mouse_points = [] 
		self.keyboard_points = []
	
	def start_logging(self):
		self.base_time = time.time()

	def save(self):
		output_file = open("mouse_events", "wb")
		pickle.dump(self.mouse_points, output_file)
		output_file.close()

		output_file = open("keyboard_events", "wb")
		pickle.dump(self.keyboard_points, output_file)
		output_file.close()

	def get_time(self):
		return time.time() - self.base_time


def start_tracking(config):
	while config.run:
		time.sleep(0.2)
		position = mouse.get_position()

		config.mouse_points.append((config.get_time(), position))

		print ((config.get_time(), position))

	config.save()

def end_tracking(config, event):
	config.run = False 

def previous_slide(config, event):
	config.keyboard_points.append((config.get_time(), 'LEFT'))

def next_slide(config, event):
	config.keyboard_points.append((config.get_time(), 'RIGHT'))

if __name__=='__main__':
	config = Config()
	config.start_logging()

	on_press_key_args('q', end_tracking, config)
	on_press_key_args('left', previous_slide, config)
	on_press_key_args('right', next_slide, config)
	Thread(target=start_tracking, args=(config, )).start()
