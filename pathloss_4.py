
import numpy as np
import matplotlib.pyplot as plt

# Distance from 1 to 100 metres
d = np.arange(1, 101, 0.1)

# Given values
c = 3 * 10**8
f1 = 800 * 10**6
f2 = 950 * 10**6

# Calculate path loss
p1 = 20*np.log10(f1) + 20*np.log10(d) + 20*np.log10(4*np.pi/c)

p2 = 20*np.log10(f2) + 20*np.log10(d) + 20*np.log10(4*np.pi/c)

# Plot graph
plt.plot(d, p1, color="red", label="800 MHz")
plt.plot(d, p2, color="blue", label="950 MHz", linestyle="--")

plt.legend()
plt.xlabel("Distance in meter")
plt.ylabel("Path loss in decibel")

plt.show()

Path loss is the reduction in signal power when a signal travels from a transmitter to a receiver over a distance.
Example
When we use Wi-Fi, the signal is strong when we stand near the router. As we move farther away, the signal becomes weaker. This is called path loss.
Why does Path Loss occur?
Path loss occurs because the energy of a transmitted signal spreads over a larger area as it travels. Therefore, the received signal power decreases with increasing distance.
Factors affecting Path Loss
1. Distance: Greater distance causes greater path loss.
2. Frequency: Higher frequency causes greater free-space path loss at the same distance.
3. Obstacles: Walls, buildings and other objects can weaken wireless signals.
4. Environment: Surrounding conditions can affect signal propagation.
Formula of Free-Space Path Loss (FSPL)
\[
FSPL(dB)=20\log_{10}\left(\frac{4\pi df}{c}\right)
\]

Where:
- d = Distance between transmitter and receiver (metres).
- f = Frequency (Hz).
- c = Speed of light (\(3\times10^8\) m/s).
- π = 3.14.
