import keyboard, mouse, time, json
import os
from zipfile import ZipFile 



def on_press_key_args(key, callback, config, suppress=False):
    return keyboard.hook_key(key, lambda e: e.event_type == keyboard.KEY_UP or callback(config, e), suppress=suppress)

class Config:
	def __init__(self, params):
		self.params = params 
		self.run = True
		self.mouse_points = [] 
		self.keyboard_points = []
		self.continue_recording = True
	
	def start_logging(self):
		self.base_time = time.time()

	def save(self):
		output_file = open(self.params["mouse"], "w")
		output_file.write(json.dumps(self.mouse_points))
		output_file.close()

		output_file = open(self.params["keyboard"], "w")
		output_file.write(json.dumps(self.keyboard_points))
		output_file.close()

	def get_time(self):
		return time.time() - self.base_time

def save(params):
	zipObj = ZipFile('output/recording.sld', 'w')

	zipObj.write(params["mouse"])
	zipObj.write(params["keyboard"])
	zipObj.write(params["audio"])

	zipObj.close()

	os.remove(params["mouse"])
	os.remove(params["keyboard"])
	os.remove(params["audio"])
	os.remove(params["audio"] + ".wav")