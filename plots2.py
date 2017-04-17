import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib import style

# style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_ylim(-4.1, 4.1)
ax1.set_xlim(0, 50)

n = 10000
L = 10

xs = [x1 / n * L for x1 in range(n)]


def animate(i):
    w = 0.13
    ys = [x1/(0.2+x1**2)*np.cos(w*i-x1) for x1 in xs]
    ax1.clear()
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, 10000, repeat=False, interval=1)
plt.show()

