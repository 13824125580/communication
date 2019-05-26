import matplotlib.pyplot as plt
import numpy as np
import seaborn

Fs = 250.0; # sampling rate采样率
Ts = 1.0/Fs; # sampling interval 采样区间
t = np.arange(0,1,Ts) # time vector,这里Ts也是步长
print(t)
ff = 25; # frequency of the signal信号频率
y = np.sin(2*np.pi*ff*t)
print(y)
print(np.sin(2*np.pi*25*0.02))
n = len(y) # length of the signal
print(n)
k = np.arange(n)
print(k)
T = n/Fs
frq = k/T # two sides frequency range
frq1 = frq[range(int(n/2))] # one side frequency range
print(frq1)
print(frq)
print("t is")
print(T)
YY = np.fft.fft(y) # 未归一化
Y = np.fft.fft(y)/n # fft computing and normalization 归一化
Y1 = Y[range(int(n/2))]

fig, ax = plt.subplots(4, 1)

ax[0].plot(t,y)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')

ax[1].plot(frq,abs(YY),'r') # plotting the spectrum
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|Y(freq)|')

ax[2].plot(frq,abs(Y),'G') # plotting the spectrum
ax[2].set_xlabel('Freq (Hz)')
ax[2].set_ylabel('|Y(freq)|')

ax[3].plot(frq1,abs(Y1),'B') # plotting the spectrum
ax[3].set_xlabel('Freq (Hz)')
ax[3].set_ylabel('|Y(freq)|')

plt.show()
