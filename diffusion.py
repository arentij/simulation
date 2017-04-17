import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def f(x):
    return 10*x*x*np.exp(-(x-L*2/3)**2/sigma**2)


def d(x):
    return 0.1


def source(xi):
    if -7 < xi - 150 < -7:
        return 10*(xi-150)**2
    else:
        return 0 + 0*f(xi)


def grad_D(xi):
    if xi == 0 or xi == n-1:
        return 0
    else:
        return (d(xi+1) - d(xi-1))/2/dx


def grad_y(xi):
    if xi == 0:
        return (y[s-1][xi+1] - edge)/2/dx
    elif xi == n-1:
        return (edge - y[s-1][xi-1])/2/dx
    else:
        return (y[s-1][xi+1] - y[s-1][xi-1])/2/dx


def lapl_y(xi):
    if xi == 0:
        return (y[s-1][xi+1] + edge - 2 * y[s-1][xi])/dx/dx
    elif xi == n-1:
        return (y[s-1][xi-1] + edge - 2 * y[s-1][xi])/dx/dx
    else:
        return (y[s-1][xi+1] + y[s-1][xi+1] - 2 * y[s-1][xi])/dx/dx


def dy(xi):
    return dt*(source(xi) + d(xi)*lapl_y(xi) + grad_D(xi)*grad_y(xi))



n = 200
L = 10
m = 1000
T = 10
sigma = 2
w = 2
k = 2
edge = 1  ## Boundary conditions
dx = L/n
dt = T/m
x = [x1*L/n for x1 in range(n)]

y = [[0 for x1 in range(n)] for t1 in range(m)]

#  initial conditions
y[0] = [f(xi) for xi in x]


for s in range(1, m):
    for xi in range(n):
        y[s][xi] = y[s-1][xi] + dy(xi)


print(y[-1])


#  animation

fig = plt.figure()
ax1 = fig.add_subplot(111)


def animate(i):
    x1 = x
    y1 = y[i]
    ax1.clear()
    ax1.plot(x1, y1)
    ax1.set_xlim([0, L])
    ax1.set_ylim([0, 150])
    print(i)


ani = animation.FuncAnimation(fig, animate, m, interval=1, repeat=True)
plt.show()