
import numpy as np
import matplotlib.pyplot as plt

Fs = 6000
t = np.arange(0, 0.05, 1/Fs)

Am = 5
fm = 100

in_signal = Am * np.sin(2 * np.pi * fm * t)

plt.subplot(3, 1, 1)
plt.plot(t, in_signal)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("input signal")

noise_power = 0.3
noise_signal = np.random.normal(0, noise_power, len(t))

plt.subplot(3, 1, 2)
plt.plot(t, noise_signal)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("noise signal")

Received_signal = in_signal + noise_signal

plt.subplot(3, 1, 3)
plt.plot(t, Received_signal, label="received noisy signal")
plt.plot(t, in_signal, "r:", label="clean input signal")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("received signal")

plt.legend()
plt.tight_layout()
plt.show()
