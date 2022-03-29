import sounddevice
from scipy.io.wavfile import write

fs = 44100
seconds = int (input ("Enter the length of the recording in seconds: "))
print("recording...\n")
myrecording = sounddevice.rec(int(seconds * fs), samplerate=fs, channels=2)
sounddevice.wait()
write("output.wav", fs, myrecording)
print("done")