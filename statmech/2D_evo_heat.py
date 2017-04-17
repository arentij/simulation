import json
from pprint import pprint
import matplotlib.pyplot as plt
import matplotlib.animation as animation



def animate(i):
    ax1.clear()
    ax1.pcolor(data[i])
    # name_png = 'shot' + str(i) + '.png'
    # if i < 0:
    #     plt.savefig(name_png)


with open('2D_time_evolution_h.json') as json_data:
    d = json.load(json_data)
    json_data.close()

# print(d.keys())

data = d['E']
beta = d['beta']
print(data[0])


fig, ax1 = plt.subplots()
heatmap = ax1.pcolor(data[0])

tm = len(beta)
ani = animation.FuncAnimation(fig, animate, tm, interval=100, repeat=False)
# plt.show()

ani.save('animation5_h_50_3.mp4', fps=30, extra_args=['-vcodec', 'libx264'])




