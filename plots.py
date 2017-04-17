import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def _update_plot(i, fig, scat):
    scat.set_offsets(([0, i], [50, i], [100, i]))
    print('Frames: %d' %i)
    return scat,


def f(x, t=0, w=3, k=1, sigma=10000):
    A = 1
    return A
    # return A*np.sin(k*x/np.sqrt(sigma)-w*t)


fig = plt.figure()

n = 500
x = [i for i in range(n)]
y = [f(x1) for x1 in x]


ax = fig.add_subplot(111)
ax.grid(True, linestyle='-', color='0.75')
ax.set_xlim([0, 10])
ax.set_ylim([-2, 2])

scat = plt.scatter(x, y, c=x)

scat.set_alpha(0.8)

anim = animation.FuncAnimation(fig, _update_plot, fargs=(fig, scat), frames=100, interval=100)

plt.show()

