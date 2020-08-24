from threading import Thread 
import mouse, time, keyboard, pickle 

from tracker import start_tracking, end_tracking, previous_slide, next_slide

from utils import Config, on_press_key_args, save

from recorder import record


if __name__=='__main__':
	params = {"mouse" : "output/mouse.json", "keyboard": "output/keyboard.json", "audio": "output/audio.mp3"}
	config = Config(params)
	config.start_logging()

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
