from threading import Thread 
import mouse, time, keyboard, pickle 

from tracker import start_tracking, end_tracking, previous_slide, next_slide

from utils import Config, on_press_key_args, save, get_resolution

from recorder import record
import json
import sys


if __name__=='__main__':
	if len(sys.argv) < 2:
		print ("Please supply pdf location")
		sys.exit(0)

	params = {"metadata":"output/metadata", "pdf":"output/slides.pdf", "mouse" : "output/mouse.json", "keyboard": "output/keyboard.json", "audio": "output/audio.mp3"}

	res = get_resolution()
	with open(params["metadata"], "w") as f:
		f.write(json.dumps(res))


	config = Config(params)
	config.start_logging()

	params["original"] = sys.argv[1]
	on_press_key_args('q', end_tracking, config)
	on_press_key_args('left', previous_slide, config)
	on_press_key_args('right', next_slide, config)

	tracker_thread = Thread(target=start_tracking, args=(config, ))
	recorder_thread = Thread(target=record, args=(config, ))

	tracker_thread.start()
	recorder_thread.start()

	tracker_thread.join()
	recorder_thread.join()

	save(params)
