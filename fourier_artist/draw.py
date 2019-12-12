import numpy as np
import matplotlib.pyplot as plt
from fourier_artist.clean_data import get_data_from_func, clean_data
from matplotlib.animation import FuncAnimation


# %%


def draw(X, fig, ax):
    n = len(X)
    x_fo = np.fft.fft(X)

    # 振幅小的剔除掉
    x_fo[np.abs(x_fo) < 1] = 0
    print('总点数{}，过滤后的有效点数{}'.format(n, (np.abs(x_fo) > 0).sum()))

    # %%

    pic_total = ax.plot(X.real, X.imag, linestyle=':', color='gray')  # 完整图像
    # X_fitted=np.fft.ifft(x) # 剔除小振幅后的图像效果，供测试用
    # ax.plot(X_fitted.real,X_fitted.imag)

    # %%
    # 已经画出来的图像，后面填充
    pic_drawn = ax.plot([0], [0], '-r')
    # n-1个圆周,后面填充
    circle_plt_list = [ax.plot([0], [0], 'y')[0] for i in range(n - 1)]
    # 直径线，后面填充
    radius_plt = ax.plot([0, 0], [0, 0], color='r', marker='o', linestyle='-')

    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(-0.5, 0.5)
    plt.ion()

    # plt.plot()

    def update_all(i):
        right = np.exp(i * 1j * 2 * np.pi * np.arange(n) / n)
        radius_points = np.cumsum(x_fo * right) / n
        plt.setp(pic_drawn, 'xdata', X[:int(i) + 1].real, 'ydata', X[:int(i) + 1].imag)  # 已经画出来的图像，用真实值
        plt.setp(radius_plt[0], 'xdata', radius_points.real, 'ydata', radius_points.imag)  # 直径线
        # n-1个圆周：
        for j in range(n - 1):
            center, radius = radius_points[j], x_fo[j + 1]
            circle_point = center + radius * np.exp(1j * np.linspace(0, 2 * np.pi, 30)) / n
            plt.setp(circle_plt_list[j], 'xdata', circle_point.real, 'ydata', circle_point.imag)
        return pic_drawn + radius_plt + circle_plt_list

    return update_all


if __name__ == '__main__':
    # 导入数据
    X = get_data_from_func()
    # 清洗数据
    X = clean_data(X)
    fig, ax = plt.subplots(1, 1)
    update_all = draw(X, fig, ax)
    ani = FuncAnimation(fig, update_all, blit=True, interval=25, frames=len(X))
    ani.save('fourier.gif', writer='pillow')
    plt.show()
