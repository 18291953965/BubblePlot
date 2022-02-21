#  来自文章：https://blog.csdn.net/qq_35189715/article/details/109288053
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

midwest = pd.read_excel(r'midwest_filter.xlsx')
print(midwest.head(10))


# 将分类category数据作为颜色标记
categories = midwest['category']
colors = [plt.cm.tab10(i/float(len(categories)-1)) for i in range(len(categories))]
# 设计绘图尺寸等细节
fig, ax = plt.subplots(1, 1, figsize=(16, 10), dpi=80)
# 绘制不同分类（category）的气泡图，气泡尺寸取决于dot_size属性
for i, category in enumerate(categories):
    data = midwest.loc[midwest['category']==category, :]
    ax.scatter('area', 'poptotal', s='dot_size', data=data,
                c=[colors[i]]*len(data), edgecolors='black', linewidths=.5, label=category)
ax.set_xlabel('Area', fontsize=14)
ax.set_ylabel('Poptotal', fontsize=14)
ax.set_title('Bubble Plot', loc='left', fontsize=16)
ax.legend(fontsize=12, labelspacing=0.8, borderpad=.7)
plt.show()






































# ————————————————
# 版权声明：本文为CSDN博主「码码的哈士奇」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_35189715/article/details/109288053