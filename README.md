## 傅里叶变换画心

### 安装
```bash
pip install fourier_artist
```

### 使用

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
ani.save('fourier.gif', writer='pillow')
# plt.show()
```


![fourier](https://github.com/guofei9987/fourier_artist/blob/master/docs/fourier.gif?raw=true)