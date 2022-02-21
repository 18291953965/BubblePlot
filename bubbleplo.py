import matplotlib.pyplot as plt
import numpy as np
# https://blog.csdn.net/weixin_48615832/article/details/108478591?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522161588469816780274160389%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=161588469816780274160389&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-4-108478591.first_rank_v2_pc_rank_v29&utm_term=bubbleplot

my_dpi = 96
plt.figure(figsize=(480 / my_dpi, 480 / my_dpi), dpi=my_dpi)

x = np.random.rand(40)
y = np.random.rand(40)
z = np.random.rand(40)

plt.scatter(x, y, s=z * 1000, alpha=0.5)
plt.show()