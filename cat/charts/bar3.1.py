from pyecharts import Bar,Grid
import pandas as pd

group01=[]
sheet0=pd.read_excel("./data_resources/3.1每组人数.xls")
group02=sheet0["组名"].values.tolist()
for i in [ "售前组","领导组","销售组","硬件组","大数据云计算组",
          "软件组", "市场商务","综合管理"]:
    group01.append((i, sheet0[i].values.tolist()))
bar0 = Bar('各组人数', title_pos="0%")
for i in group01:
    if i[1] is not None:
        bar0.add(i[0],group02,i[1], xaxis_rotate=30, yaxis_name='出差数(元/人)', yaxis_name_pos='middle',yaxis_name_gap=50, legend_pos="40%", legend_top="2%", is_label_show=True,label_pos='inside', is_stack=True)
bar0.render("./all_charts/"+"3.1每组人数" + ".html")