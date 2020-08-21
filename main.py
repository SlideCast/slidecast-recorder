from threading import Thread 
import mouse, time, keyboard, pickle 

from tracker import start_tracking, end_tracking, previous_slide, next_slide

from utils import Config, on_press_key_args

from recorder import record


if __name__=='__main__':
	params = {"mouse" : "output/mouse.json", "keyboard": "output/keyboard.json", "audio": "output/audio.wav"}
	config = Config(params)
	config.start_logging()

	on_press_key_args('q', end_tracking, config)
	on_press_key_args('left', previous_slide, config)
	on_press_key_args('right', next_slide, config)
	Thread(target=start_tracking, args=(config, )).start()
	Thread(target=record, args=(config, )).start()