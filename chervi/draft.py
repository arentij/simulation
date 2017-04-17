import matplotlib.pyplot as plt


def vx(x, y):
    a = 10
    return 1/a


def vy(x, y):
    b = 10
    return y/b


L = 10
x = [L/3]
y = [L/3]
N = 1000
dt = 0.02


for i in range(N):

    xi = (L + x[i]+dt*vx(x[i], y[i])) % L
    x.append(xi)

    yi = (L + y[i] + dt * vy(x[i], y[i])) % L
    y.append(yi)

# for i in range(len(x)):
#     print(x[i], y[i])
print(*x)

plt.plot(x, y)
# plt.axes([0, L, 0, L])
plt.show()
