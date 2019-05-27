#sound_proc.py
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

sampFreq, snd = wavfile.read('440_sine.wav')
print(snd.shape)
print(sampFreq)
snd = snd / (2.**15)
s1 = snd[:,1]

#Calc data for subplot 1
timeArray = np.arange(0, 5292.0, 1)
timeArray = timeArray / sampFreq
timeArray = timeArray * 1000

#Calc data for subplot 2
n = len(s1)
print(n)
p = np.fft.fft(s1)
nUniquePts = np.ceil((n + 1) / 2.0)
nUnique = 2647;
p = p[0:nUnique]
p = abs(p)

p = p / float(n)
p = p ** 2

if n % 2 > 0:
	p[1:len(p)] = p[1 : len(p)] * 2;
else:
	p[1:len(p) - 1] = p[1 : len(p) - 1] * 2

freqArray = np.arange(0, nUnique, 1.0) * (sampFreq / n)

#plot
plt.subplot(2, 1, 1)
plt.title('Basic Sound Processing w/ Python')
plt.plot(timeArray, s1, color = 'y')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(freqArray / 1000, 10 * np.log10(p), color = 'r')
plt.xlabel('Frequency (kHz)')
plt.ylabel('Power (dB)')
plt.show()
