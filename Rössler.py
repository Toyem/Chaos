import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def rossler(x, y, z, a=0.2, b=0.2, c=5.7):
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       a, b, c: parameters defining the Rössler attractor
    Returns:
       x_dot, y_dot, z_dot: values of the rossler attractor's partial
           derivatives at the point x, y, z
    '''
    x_dot = - y - z
    y_dot = x +a*y
    z_dot = b+z*(x-c)
    return x_dot, y_dot, z_dot


print("Enter the dt (the step)")
print("Best values are around 0.01")
dt = float(input(""))
print("Enter the number of step")
print("Best values are greater than 10000")
num_steps = int(input(""))

# Need one more for the initial values
xs = np.empty((num_steps + 1,))
ys = np.empty((num_steps + 1,))
zs = np.empty((num_steps + 1,))

# Set initial values
xs[0] = float(input("Set the x value (best 0): "))
xs[0] = float(input("Set the y value (best 0): "))
xs[0] = float(input("Set the z value (best 0): "))

# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point
for i in range(num_steps):
    x_dot, y_dot, z_dot = rossler(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)


# Plot
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(xs, ys, zs, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Rossler Attractor")

plt.show()
