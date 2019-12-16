

<table border="0" width="10%">
  <tr>
    <td><img src="https://github.com/guofei9987/pictures_for_blog/blob/master/tmp/1.jpg?raw=true" height="80" width="82"></td>
    <td><img src="https://github.com/guofei9987/pictures_for_blog/blob/master/tmp/2.jpg?raw=true" height="80" width="82"></td>
    <td><img src="https://github.com/guofei9987/pictures_for_blog/blob/master/tmp/3.jpg?raw=true" height="80" width="82"></td>
  </tr>
  <tr>
    <td><img src="https://github.com/guofei9987/pictures_for_blog/blob/master/tmp/4.jpg?raw=true" height="80" width="82"></td>
    <td><img src="https://img.shields.io/github/stars/guofei9987/fourier_artist.svg?style=social"></td>
    <td><img src="https://github.com/guofei9987/pictures_for_blog/blob/master/tmp/6.jpg?raw=true" height="82" width="82"></td>
  </tr>
   <tr>
    <td><img src="https://github.com/guofei9987/pictures_for_blog/blob/master/tmp/7.jpg?raw=true" height="82" width="82"></td>
    <td><img src="https://github.com/guofei9987/pictures_for_blog/blob/master/tmp/8.jpg?raw=true" height="82" width="82"></td>
    <td><img src="https://github.com/guofei9987/pictures_for_blog/blob/master/tmp/9.jpg?raw=true" height="82" width="82"></td>
  </tr>
</table>

## 用几个圆画任意图

[![PyPI](https://img.shields.io/pypi/v/fourier_artist)](https://pypi.org/project/fourier_artist/)
[![Build Status](https://travis-ci.com/guofei9987/fourier_artist.svg?branch=master)](https://travis-ci.com/guofei9987/fourier_artist)
[![codecov](https://codecov.io/gh/guofei9987/fourier_artist/branch/master/graph/badge.svg)](https://codecov.io/gh/guofei9987/fourier_artist)
[![License](https://img.shields.io/pypi/l/fourier_artist.svg)](https://github.com/guofei9987/fourier_artist/blob/master/LICENSE)
![Python](https://img.shields.io/badge/python->=3.5-green.svg)
![Platform](https://img.shields.io/badge/platform-windows%20|%20linux%20|%20macos-green.svg)
[![Join the chat at https://gitter.im/guofei9987/fourier_artist](https://badges.gitter.im/guofei9987/fourier_artist.svg)](https://gitter.im/guofei9987/fourier_artist?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


### 安装
```bash
pip install fourier_artist
```

### 示例：傅里叶变换画心
（随便画几个圈都是爱你的样子）

```python
# 导入包
import numpy as np
import matplotlib.pyplot as plt
from fourier_artist.clean_data import get_data_from_func, clean_data
from fourier_artist.draw import draw
from matplotlib.animation import FuncAnimation


# 导入数据，这个X你可以自己制定画什么图
X = get_data_from_func()
# 清洗数据
X = clean_data(X)
fig, ax = plt.subplots(1, 1)
update_all = draw(X, fig, ax)
ani = FuncAnimation(fig, update_all, blit=True, interval=25, frames=len(X))
# ani.save('fourier.gif', writer='pillow')
plt.show()
```


![fourier](docs/fourier.gif?raw=true)

## draw everything you like
```python
import numpy as np
import matplotlib.pyplot as plt
from fourier_artist.clean_data import get_data_from_func, clean_data
from fourier_artist.draw import draw
from matplotlib.animation import FuncAnimation

# 导入数据
X = get_data_from_func()

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
# ani.save('demo2.gif', writer='pillow')
plt.show()
```


![demo2](docs/demo2.gif)
