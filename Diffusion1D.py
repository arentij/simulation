import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def y0():
    a = [0]*n
    for xj in range(n):
        x = xj*L/n
        a[xj] = x*(L-x)
    return a


def source(xi):
    x = xi*L/n
    return 0


def d(xi):
    sigmad = 15
    d0 = 11
    if xi < 0:
        return 0
    elif xi >= n:
        return 0
    else:
        return d0*(2-np.exp(-1*y(xi)**2/sigmad**2))



def y(xi):      # just calling a value of function at current moment at xj and including boundary condition
    if xi < 0:
        return edge
    elif xi >= n:
        return edge
    else:
        return yt[s][xi]


def derivatives(f):
    dfdx = [0] * n
    d2dx2 = [0] * n
    dDdx = [0]*n
    for i in range(n):
        # print(i)
        dfdx[i] = (f(i + 1) - f(i - 1)) / 2 / dx
        d2dx2[i] = (f(i + 2) + f(i - 2) - 2 * f(i)) / (2 * dx) ** 2
        dDdx[i] = (d(i + 1) - d(i - 1)) / 2 / dx
    dDdx[0] = 0
    dDdx[n-1] = 0
    return dfdx, d2dx2, dDdx


def dy(xi):
    return dt * (source(xi) +  dddx[xi]*dydx[xi])
    # return dt



#  Size
n = 200
L = 10
m = 1000
T = 100
dx = L/n
dt = T/m

edge = 1  # Boundary conditions

#  creating the x grid
xg = [x1*L/n for x1 in range(n)]

# y-time evolution matrix
yt = [[0 for x1 in range(n)] for t1 in range(m)]

# starting from initial condition and determining yt[0]
s = 0
yt[s] = y0()

# calling derivatives function (dy/dx , d2y/dx , dD/dx)
dydx, lapy, dddx = derivatives(y)


for s in range(0, m-1):
    for xi in range(n):
        yt[s+1][xi] = y(xi) + dy(xi)


def animate(i):
    x1 = xg
    y1 = yt[i]
    ax1.clear()
    ax1.plot(x1, y1)
    ax1.set_xlim([0, L])
    # ax1.set_ylim([0, 150])


fig = plt.figure()
ax1 = fig.add_subplot(111)


ani = animation.FuncAnimation(fig, animate, m, interval=1, repeat=True)
plt.show()


'''


# plt.plot(xg[1:-1],[d(xi) for xi in range(1,n-1)])
# plt.plot(xg[1:-1],dddx[1:n-1])
# plt.show()


#  initial conditions
yt[0] = [0]*n

# main simulation

for s in range(1, m):
    for xi in range(n):
        y[s][xi] = y[s-1][xi] + dy(xi)


print(y[-1])


#  animation


'''