import numpy as np
import matplotlib.pyplot as plt
from fourier_artist.clean_data import get_data_from_func, clean_data
from fourier_artist.draw import draw
from matplotlib.animation import FuncAnimation

# 导入数据
X = get_data_from_func()
# 清洗数据
X = clean_data(X)
fig, ax = plt.subplots(1, 1)
update_all = draw(X, fig, ax)
ani = FuncAnimation(fig, update_all, blit=True, interval=25, frames=len(X))
ani.save('fourier.gif', writer='pillow')
# plt.show()
