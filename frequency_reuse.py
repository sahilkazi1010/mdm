
import numpy as np
import matplotlib.pyplot as plt

# Given values
N = 7
R = 2

# Calculate reuse distance
D = R * np.sqrt(3*N)

print("Reuse Distance:", round(D, 3))

# Three cell positions
cx = [0, D, D/2]
cy = [0, 0, 0.866*D]

# Function to draw hexagon
def hexagon(x1, y1, r):
    x = [x1-r, x1-r/2, x1+r/2,
         x1+r, x1+r/2, x1-r/2, x1-r]

    y = [y1, y1+0.866*r, y1+0.866*r,
         y1, y1-0.866*r, y1-0.866*r, y1]

    plt.fill(x, y, color="orange", alpha=0.5)
    plt.plot(x, y, "k-")

# Draw three cells
for i in range(3):
    hexagon(cx[i], cy[i], R)
    plt.text(cx[i], cy[i], "f1", ha="center")

# Connect cell centres
plt.plot(cx, cy, "b--", marker="o")

# Display distance
plt.text(D/2, 0.2, "D = " + str(round(D, 3)))

plt.xlabel("Horizontal Distance")
plt.ylabel("Vertical Distance")
plt.title("Frequency Reuse (N=7)")
plt.axis("equal")
plt.grid()
plt.show()
