import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def f(xi, ti):
    x = xi*L/n
    t = ti*T/m
    sigma = 3
    return x*x * np.exp(-(x-L/3)**2/sigma**2) * (1+np.cos(w*t-k*x))

n = 1000
L = 10
m = 1000
T = 10

w = 2
k = 2

x = [x1*L/n for x1 in range(n)]
y = [[f(x1, t1) for x1 in range(n)] for t1 in range(m)]
t = 0

fig = plt.figure()
ax1 = fig.add_subplot(111)


def animate(i):
    xi = x
    yi = y[i]
    ax1.clear()
    ax1.plot(x, yi)
    ax1.set_xlim([0, L])
    ax1.set_ylim([0, 40])
    print(i)


ani = animation.FuncAnimation(fig, animate, m, interval=1, repeat=True)
plt.show()
