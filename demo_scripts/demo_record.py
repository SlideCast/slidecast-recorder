import pyaudio
import wave, keyboard

def on_press_key_args(key, callback, config, suppress=False):
    return keyboard.hook_key(key, lambda e: e.event_type == keyboard.KEY_UP or callback(config, e), suppress=suppress)

cont = True 
def record():

	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 84100
	CHUNK = 1024
	RECORD_SECONDS = 10
	WAVE_OUTPUT_FILENAME = "file.wav"
	 
	audio = pyaudio.PyAudio()
	 
	# start Recording
	stream = audio.open(format=FORMAT, channels=CHANNELS,
	                rate=RATE, input=True,
	                frames_per_buffer=CHUNK)
	print ("recording...")
	frames = []
	 
	while cont:
	    data = stream.read(CHUNK)
	    frames.append(data)
	print ("finished recording")
	 
	 
	# stop Recording
	stream.stop_stream()
	stream.close()
	audio.terminate()
	 
	waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	waveFile.setnchannels(CHANNELS)
	waveFile.setsampwidth(audio.get_sample_size(FORMAT))
	waveFile.setframerate(RATE)
	waveFile.writeframes(b''.join(frames))
	waveFile.close()

def end_tracking(config, event):
	global cont 
	cont = False


if __name__=='__main__':

	on_press_key_args('q', end_tracking, 1)
	record()