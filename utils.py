import keyboard, mouse, time, json
import os
from zipfile import ZipFile 
import shutil


def get_resolution():
	import tkinter as tk

	root = tk.Tk()
	width = root.winfo_screenwidth()
	height = root.winfo_screenheight()

	return {"width":width, "height":height}
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
	shutil.copyfile(params["original"], params["pdf"])
	zipObj = ZipFile('output/recording.sld', 'w')

	zipObj.write(params["mouse"])
	zipObj.write(params["keyboard"])
	zipObj.write(params["audio"])
	zipObj.write(params["pdf"])
	zipObj.write(params["metadata"])
	zipObj.close()

	os.remove(params["mouse"])
	os.remove(params["pdf"])
	os.remove(params["keyboard"])
	os.remove(params["audio"])
	os.remove(params["metadata"])
	os.remove(params["audio"] + ".wav")

if __name__=='__main__':
	print (get_resolution())