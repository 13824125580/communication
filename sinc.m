dt=0.01;
fs=1/dt;
t=-100:dt:100-dt
sinct=sin(pi*t)./(pi*t);
subplot(2,1,1)
plot(t,sinct)
xlim([-8,8])
N=2^20*32;
sincf=fft(sinct,N);
f=-fs/2:fs/N:(fs/2-fs/N);
subplot(2,1,2)
plot(f,fftshift(abs(sincf))/max(abs(sincf)))
axis([-10 10,0,1]);
