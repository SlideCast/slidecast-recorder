from pydub import AudioSegment
recording = AudioSegment.from_wav("audio.wav")
recording.normalize()
recording.export("audio.mp3")