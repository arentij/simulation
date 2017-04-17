import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def f(xc, yc):
    x = xL*xc/xm
    y = yL*yc/ym
    return ((x-xL/2)**2 + (y-yL/2)**2)**0.5


def animate(i):
    ax1.clear()
    ax1.pcolor(data[i])


def d_data():
    return [[f(x, y)**0.2/10 for x in range(xm)] for y in range(ym)]

kx = 2
ky = 2
w = 0.1
xm = 100
ym = 100
tm = 100
xL = 10
yL = 10
tL = 10

data = [[[x+y for x in range(xm)] for y in range(ym)] for P in range(tm)]
data[0] = [[f(x, y) for x in range(xm)] for y in range(ym)]


for t in range(1, tm):
    a = d_data()
    for yi in range(ym):
        for xi in range(xm):

            data[t][yi][xi] = data[t-1][yi][xi] + a[yi][xi]



fig, ax1 = plt.subplots()
heatmap = ax1.pcolor(data[0])

ani = animation.FuncAnimation(fig, animate, tm, interval=1, repeat=False)
plt.show()



