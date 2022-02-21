import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np; np.random.seed(0)
import pandas as pd

#设置绘图风格
plt.style.use('ggplot')
#处理中文乱码
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
#坐标轴负号的处理
plt.rcParams['axes.unicode_minus']=False
# 去掉网格线
plt.rcParams["axes.grid"] = False

# 读取数据
Prod_Category = pd.read_excel(r'某超市的商品类别销售数据.xlsx')

x =x= Prod_Category.Sales[Prod_Category.Category == '办公用品'] #水库水位
y =Prod_Category.Profit[Prod_Category.Category == '办公用品']  #降雨
c = Prod_Category.Profit_Ratio[Prod_Category.Category == '办公用品'] #水库水位 变化


cmap = plt.cm.rainbow
norm = matplotlib.colors.Normalize(vmin=np.min(Prod_Category.b2), vmax=np.max(Prod_Category.b2))




fig, ax = plt.subplots()
ax.spines['bottom'].set_visible(True)
ax.spines['bottom'].set_color('black')

ax.spines['left'].set_visible(True)
ax.spines['left'].set_color('black')
bubble = ax.scatter(x= Prod_Category.Sales[Prod_Category.Category == '办公用品'],
           y = Prod_Category.Profit[Prod_Category.Category == '办公用品'],
           s = Prod_Category.Profit_Ratio[Prod_Category.Category == '办公用品']*4,
           color=cmap(norm(Prod_Category.b2.values)), alpha =0.8,label = '位移速率(mm/月)',
          edgecolors = 'k');# 上面这一行*4是在控制大、
#ax.set_xticks(x)

# 设置背景颜色为白色 如果有这一步 那就不能绘制网格 plt.grid不生效了
#ax.set_facecolor("WHITE")

plt.grid();
plt.title("滑坡位移速率和降雨量以及水库水位变化之间的关系")
plt.ylabel('降雨量(mm)')
plt.xlabel('水库水位(m)')

plt.legend();
plt.xlim((140,180));
plt.ylim((0,350));

sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
#在实验室电脑上sm.set_array([])是注释的


#设置colorbar的标签字体及其大小
cb=fig.colorbar(sm)
cb.set_label('水库水位变化量(m/月)')

#解决中文乱码问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False




plt.savefig("temp.png",dpi=1500,bbox_inches = 'tight')#解决图片不清晰，不完整的问题
plt.savefig("20220219.jpg")
plt.show()# 生成图片 的  必须得有

