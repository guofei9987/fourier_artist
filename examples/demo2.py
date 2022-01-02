import matplotlib.pyplot as plt
from fourier_artist.clean_data import get_data_from_func, clean_data
from fourier_artist.draw import draw
from matplotlib.animation import FuncAnimation
import numpy as np

n = 100
t = np.linspace(0, 2 * np.pi, n)
x = (np.sin(t)) ** 2
y = (np.cos(t)) ** 2 + np.cos(t)
X = x + 1j * y

# 清洗数据
X = clean_data(X)
fig, ax = plt.subplots(1, 1)
update_all = draw(X, fig, ax)
ani = FuncAnimation(fig, update_all, blit=True, interval=25, frames=len(X))
ani.save('demo2.gif', writer='pillow')
# plt.show()
