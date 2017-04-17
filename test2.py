import matplotlib.pyplot as plt
import numpy as np

dt = 1/256
Fs = 1/dt
t = np.arange(0, 10, dt)
# nse = np.random.randn(len(t))
# r = np.exp(-t/0.05)

# cnse = np.convolve(nse, r)*dt
# cnse = cnse[:len(t)]
s = 0.1*np.sin(100*np.pi*t) + 0.1*np.sin(150*np.pi*t)

plt.subplot(3, 2, 1)
plt.plot(t, s)

plt.subplot(3, 2, 3)
plt.magnitude_spectrum(s, Fs=Fs)

plt.subplot(3, 2, 4)
plt.magnitude_spectrum(s, Fs=Fs, scale='dB')

plt.subplot(3, 2, 5)
plt.angle_spectrum(s, Fs=Fs)

plt.subplot(3, 2, 6)
plt.phase_spectrum(s, Fs=Fs)

plt.show()