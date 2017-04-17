import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

# print(np.cross(x, y))
# print(np.dot(x, y))


def c():
    x = np.cross(v, Omega)
    x = np.multiply(0.5, x)
    x = np.add(Sigma, x)
    x = np.multiply(dt, x)
    x = np.add(v, x)
    return x


def a():
    return np.multiply(Omega, dt/2)


def v1():
    x = np.cross(c(), a())
    x2 = np.multiply(a(), np.dot(a(), c()))
    x = np.add(x, x2)
    x = np.add(c(), x)
    x = np.multiply(1/(1+np.dot(a(), a())), x)
    return x


def bfield():
    return [0, 0, 0]


def efield():
    # x = r[0] y = r[1] z = r[2]
    ff = k/rad2()
    dx = r[0] - xc
    dy = r[1] - yc
    dz = r[2] - zc

    fx = ff*dx/rad2()**0.5
    fy = ff*dy/rad2()**0.5
    fz = ff*dz/rad2()**0.5

    return [fx, fy, fz]


def rad2():
    return (r[0]-xc)**2 + (r[1]-yc)**2 + (r[2]-zc)**2


# charge
k = 1
xc = 0
yc = 0
zc = 0


v = [0, 1, 0]
r = [0, 0, 1]
# B = [0, 0, 0]
# E = [0, 0, 0]
q = 1
m = 1
dt = 0.01

state = [r]
# state.append(r)


# print(np.add(B, np.add(E, r)))
steps = 20000
for i in range(steps):
    E = efield()
    B = bfield()

    Omega = np.multiply(q / m, B)
    Sigma = np.multiply(q / m, E)

    v = v1()
    r = np.add(r, np.multiply(v, dt))
    state.append(r)
    # print('r=', r, 'r2=', rad2())
    if rad2() > 1000:
        break

    # print(np.dot(Sigma, Sigma))
    # print(np.cross(Sigma, Omega))

    # xs = r[0]
    # ys = r[1]
    # zs = r[2]


# _________________________

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()

ax = fig.gca(projection='3d')
ax2 = fig.gca(projection='3d')
# theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = [x[2] for x in state]
x = [x[0] for x in state]
y = [x[1] for x in state]
ax.plot(x, y, z, label='parametric curve')
ax.legend()
ax2.scatter([xc, xc], [yc, yc], [zc, zc])
plt.show()



