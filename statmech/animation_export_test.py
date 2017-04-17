import matplotlib.animation as animation
import numpy as np
from pylab import *
import json


dpi = 100

def ani_frame():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax1.pcolor(data[0])

    # im = ax.imshow(heatmap, aspect='auto')
    # im.set_clim([0, 1])
    # fig.set_size_inches([5, 5])

    tight_layout()

    def update_img(n):

        # tmp = np.random.rand(300,300)
        ax1.set_data(data[0])
        return ax1

    #legend(loc=0)
    ani = animation.FuncAnimation(ax1, update_img, 300, interval=30)
    writer = animation.writers['ffmpeg'](fps=30)

    ani.save('demo.mp4', writer=writer, dpi=dpi)
    return ani



with open('2D_time_evolution_strings.json') as json_data:
    d = json.load(json_data)
    json_data.close()
data = d['E']

fig, ax1 = plt.subplots()
heatmap = ax1.pcolor(data[0])


ani_frame()
