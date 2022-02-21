import pandas as pd
import matplotlib.pyplot as plt

#设置绘图风格
plt.style.use('ggplot')
#处理中文乱码
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
#坐标轴负号的处理
plt.rcParams['axes.unicode_minus']=False
# 读取数据
Prod_Category = pd.read_excel(r'某超市的商品类别销售数据.xlsx')
# 将利润率标准化到[0,1]之间（因为利润率中有负数），然后加上微小的数值0.001
range_diff = Prod_Category.Profit_Ratio.max()-Prod_Category.Profit_Ratio.min()
Prod_Category['std_ratio'] = (Prod_Category.Profit_Ratio-Prod_Category.Profit_Ratio.min())/range_diff + 0.001

# 这里四行  是让颜色变得更加多样化  不止绿色
import matplotlib.cm as cm
import numpy as np
N=72
#colors=cm.rainbow(np.random.rand(N));



#尝试 画出colorbar
    #seed=np.random.seed(42)
    #data=np.random.randint(0,10,size=(10,10))
seed=np.random.seed(1);
# 这里的data是三原色
data = cm.rainbow(np.random.rand(N));# 本行是多加的   https://blog.csdn.net/weixin_43718675/article/details/89451587


# 绘制办公用品的气泡图
plt.scatter(x = Prod_Category.Sales[Prod_Category.Category == '办公用品'],
           y = Prod_Category.Profit[Prod_Category.Category == '办公用品'],
           s = Prod_Category.std_ratio[Prod_Category.Category == '办公用品']*1000,
           color = data, alpha = 0.7,label = 'displacement velocity(mm/month)'
            );

h=plt.contourf(data)# b2-->data
cb=plt.colorbar(h,fraction=0.03, pad=0.06)
# 设置colorbar 的刻度 从最小开始 到最大结束
cb.set_ticks([np.min(data), 0.25,0.5, 0.75, np.max(data)])

# colorbar上的刻度值个数
import matplotlib.ticker as ticker
tick_locator = ticker.MaxNLocator(nbins=5)

# 查看最大值和最小值
print(np.min(Prod_Category.b2))
print(np.max(Prod_Category.b2))
# 给colorbar 设置刻度

#cb.set_ticks([np.min(Prod_Category.b2), 0.25,0.5, .75, np.max(Prod_Category.b2)])
# cb.set_ticklabels( ('-15', '-10.5', '-6', '-1.5', '3',  '7.5',  '12',  '16.5'))


#设置colorbar的标签字体及其大小 https://blog.csdn.net/weixin_43718675/article/details/89451587?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-1&spm=1001.2101.3001.4242
cb.set_label('Change in reservoir level(m/month)')


# # 绘制技术产品的气泡图
# plt.scatter(x = Prod_Category.Sales[Prod_Category.Category == '技术产品'],
#            y = Prod_Category.Profit[Prod_Category.Category == '技术产品'],
#            s = Prod_Category.std_ratio[Prod_Category.Category == '技术产品']*1000,
#            color = 'indianred' , label = '技术产品', alpha = 0.6
#           )
# # 绘制家具产品的气泡图
# plt.scatter(x = Prod_Category.Sales[Prod_Category.Category == '家具产品'],
#            y = Prod_Category.Profit[Prod_Category.Category == '家具产品'],
#            s = Prod_Category.std_ratio[Prod_Category.Category == '家具产品']*1000,
#            color = 'green' , label = '家具产品', alpha = 0.6
#           )






# 添加x轴和y轴标签
plt.xlabel('Reservoir level(m)')
plt.ylabel('Rainfall(mm)')
# 添加标题
# plt.title('The correlation between the displacement velocity of ZG118 and the change of rainfall and reservoir  level')

# 关闭表格
#plt.grid();
plt.plot();

# 添加图例
plt.legend()
#设置纵坐标的刻度范围
plt.xlim((140,180));
plt.ylim((0, 250));
# 显示图形
plt.show()


# ————————————————
# 版权声明：本文为CSDN博主「Fo*(Bi)」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_48615832/article/details/108478591