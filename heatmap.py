import matplotlib.pyplot as plt
import numpy as np
column_labels = list('ABCD')
row_labels = list('WXYZ')
data = [[1+x*y for x in range(100)] for y in range(100)]
fig, ax = plt.subplots()
heatmap = ax.pcolor(data)

print(type(data))
# put the major ticks at the middle of each cell, notice "reverse" use of dimension


ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(column_labels, minor=False)
plt.show()