import cv2
import matplotlib.pyplot as plt
import numpy as np
import copy

# %%
# image = cv2.imread('github.jpeg', cv2.IMREAD_GRAYSCALE)
image = cv2.imread('github.JPG', cv2.IMREAD_GRAYSCALE)

# 二值化
retval, image = cv2.threshold(image, thresh=127, maxval=255, type=0)  # 二值化

# %%
# plt.imshow(image, cmap='gray')

# %%提取轮廓

contours, hierarchy = cv2.findContours(image=image, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)

image_contour = cv2.drawContours(image=np.zeros_like(image, dtype=np.uint8),
                                 contours=contours, contourIdx=-1,
                                 color=(255, 255, 255), thickness=2)
plt.imshow(image_contour, cmap='gray')

# %%
contours_choose = contours[0].reshape(-1, 2)
fig, ax = plt.subplots()
ax.plot(contours_choose[:, 0], contours_choose[:, 1])
plt.show()
# %%
# 按照最大距离，寻找起始点和终止点


num_contours_choose = contours_choose.shape[0]
distances = np.zeros(num_contours_choose)

for i in range(num_contours_choose - 1):
    distances[i] = np.linalg.norm(contours_choose[i + 1, :] - contours_choose[i, :], ord=2)

distances[num_contours_choose - 1] = \
    np.linalg.norm(contours_choose[0, :] - contours_choose[num_contours_choose - 1, :], ord=2)

# %%
max_idx = distances.argmax()
new_contours_choose = np.zeros_like(contours_choose)
if max_idx == num_contours_choose - 1:
    pass
else:
    new_contours_choose[num_contours_choose - max_idx - 1:, :] = contours_choose[:max_idx + 1, :]
    new_contours_choose[:num_contours_choose - max_idx - 1, :] = contours_choose[max_idx + 1:, :]

# %%

new_contours_choose.reshape(-1, 1, 2)
image_contour = cv2.drawContours(image=np.zeros_like(image, dtype=np.uint8),
                                 contours=[new_contours_choose], contourIdx=-1,
                                 color=(255, 255, 255), thickness=2)
plt.imshow(image_contour, cmap='gray')
# %%

X = new_contours_choose[:, 0] + 1j * new_contours_choose[:, 1]
X = -X

# %%
import numpy as np
import matplotlib.pyplot as plt
from fourier_artist.clean_data import get_data_from_func, clean_data
from fourier_artist.draw import draw
from matplotlib.animation import FuncAnimation

# %%
X = clean_data(X)

# %%
fig, ax = plt.subplots(1, 1)
update_all = draw(X, fig, ax,MAX_NUM=20)

# %%
ani = FuncAnimation(fig, update_all, blit=True, interval=25, frames=len(X))
# ani.save('fourier.gif', writer='pillow')
plt.show()


# %%
