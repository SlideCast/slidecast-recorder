import pyaudio
import wave

def record(config):

	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 84100
	CHUNK = 1024
	RECORD_SECONDS = 10
	WAVE_OUTPUT_FILENAME = config.params["audio"]
	 
	audio = pyaudio.PyAudio()
	 
	stream = audio.open(format=FORMAT, channels=CHANNELS,
	                rate=RATE, input=True,
	                frames_per_buffer=CHUNK)
	print ("recording...")
	frames = []
	 
	while config.continue_recording:
	    data = stream.read(CHUNK)
	    frames.append(data)
	print ("finished recording")
	 
	stream.stop_stream()
	stream.close()
	audio.terminate()
	 
	waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	waveFile.setnchannels(CHANNELS)
	waveFile.setsampwidth(audio.get_sample_size(FORMAT))
	waveFile.setframerate(RATE)
	waveFile.writeframes(b''.join(frames))
	waveFile.close()
	print ("saved")
