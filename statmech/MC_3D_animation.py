import json
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D


def lists_coord_e(ar):
    coord_e = {-6: [[], [], []], -4: [[], [], []], -2: [[], [], []], 0: [[], [], []], 2: [[], [], []], 4: [[], [], []], 6: [[], [], []]}

    for i in range(L):
        for j in range(L):
            for k in range(L):
                e_state = ar[i][j][k]
                coord_e[e_state][0].append(i)
                coord_e[e_state][1].append(j)
                coord_e[e_state][2].append(k)
    return coord_e


def animate(i):
    ax.clear()
    raw = lists_coord_e(data[i])

    x = raw[E][0][0:-1:]
    y = raw[E][1][0:-1:]
    z = raw[E][2][0:-1:]
    ax.scatter(x, y, z, label=E, s=0.01, c='green')

    ax.scatter([0, 50, 0, 0], [0, 0, 50, 0], [0, 0, 0, 50], label='borders', c='black')

    # x2 = raw[E2][0][0:-1:50]
    # y2 = raw[E2][1][0:-1:50]
    # z2 = raw[E2][2][0:-1:50]
    # ax2.scatter(x2, y2, z2, label=E2, c='blue')

    # x3 = raw[E3][0][0:-1:10]
    # y3 = raw[E3][1][0:-1:10]
    # z3 = raw[E3][2][0:-1:10]
    # ax3.scatter(x3, y3, z3, label=E3, c='red')

    ax.legend()

    ax.autoscale(enable=False)

with open('MC_3D_Estates_L50_b015_025_2L.json') as json_data:
    d = json.load(json_data)
    json_data.close()

# print(d.keys())

data = d['E']
beta = d['beta']

L = len(data[0][0][0])

# print(data[0][0])

# print(lists_coord_e(data[0]))



# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()

ax = fig.gca(projection='3d')
ax2 = fig.gca(projection='3d')
ax3 = fig.gca(projection='3d')


raw = lists_coord_e(data[0])
E = 4
x = raw[E][0]
y = raw[E][1]
z = raw[E][2]
# ax.scatter(x, y, z, label='E', c='green')

E2 = -6
x2 = raw[E2][0]
y2 = raw[E2][1]
z2 = raw[E2][2]
# ax2.scatter(x2, y2, z2, label=E2, c='blue')

E3 = 6
x3 = raw[E3][0]
y3 = raw[E3][1]
z3 = raw[E3][2]
# ax2.scatter(x3, y3, z3, label=E3, c='red')

ax.legend()

tm = len(beta)
ani = animation.FuncAnimation(fig, animate, tm, interval=10, repeat=False)

# plt.show()


# !!!!!!!!!!!!!!!!!!!!!!!!!!
# writing a video
# fig, ax1 = plt.subplots()
# heatmap = ax1.pcolor(data[0])
#
# tm = len(beta)
# ani = animation.FuncAnimation(fig, animate, tm, interval=100, repeat=False)
# plt.show()
#
ani.save('D3d.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
