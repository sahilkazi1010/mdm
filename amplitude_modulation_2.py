
import numpy as np
import matplotlib.pyplot as plt

# Time values
Fs = 10000
t = np.arange(0, 0.05, 1/Fs)

# Message signal
Am = 1
fm = 50
message = Am * np.sin(2 * np.pi * fm * t)

# Carrier signal
Ac = 2
fc = 500
carrier = Ac * np.sin(2 * np.pi * fc * t)

# Amplitude Modulation
modulation_index = 0.5
AM_signal = Ac * (1 + modulation_index * np.sin(2 * np.pi * fm * t)) * np.sin(2 * np.pi * fc * t)

# Plot message signal
plt.subplot(3, 1, 1)
plt.plot(t, message)
plt.title("Message Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()

# Plot carrier signal
plt.subplot(3, 1, 2)
plt.plot(t, carrier)
plt.title("Carrier Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()

# Plot AM signal
plt.subplot(3, 1, 3)
plt.plot(t, AM_signal)
plt.title("Amplitude Modulated Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()
