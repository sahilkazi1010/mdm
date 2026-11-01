import numpy as np
import matplotlib.pyplot as plt

# Distance from Wi-Fi router
distance = np.array([1, 2, 5, 10, 15, 20])

# Wi-Fi signal strength in dBm
signal = np.array([-30, -40, -50, -60, -68, -75])

# Display observation
print("Distance    Signal Strength")

for i in range(len(distance)):
    print(distance[i], "m       ", signal[i], "dBm")

# Plot graph
plt.plot(distance, signal, marker='o')

plt.xlabel("Distance (meters)")
plt.ylabel("Signal Strength (dBm)")
plt.title("Wi-Fi Signal Strength vs Distance")

plt.grid()
plt.show()
