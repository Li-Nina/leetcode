from pyecharts import Bar, Grid
import pandas as pd

# group = []
# sheet = pd.read_excel("./data_resources/2.1每个人的出差天数统计.xls")
# people = sheet["出差人"].values.tolist()
# for i in ["领导组", "硬件组", "销售组", "售前组",
#           "软件组", "大数据云计算组"]:
#     group.append((i, sheet[i].values.tolist()))
#
# bar = Bar('个人出差人天数排名')
# for i in group:
#     bar.add(i[0], people, i[1],xaxis_rotate = 40, is_label_show = True, label_pos= 'inside',label_text_size=8,yaxis_name = '出差数(天)',yaxis_name_pos = 'middle',yaxis_name_gap = 40,legend_pos='15%', is_stack=True)
# # bar.add(i[0], people, i[1],xaxis_rotate = 40, label_pos = 'inside',label_text_size=6,yaxis_name = '出差数(天)',yaxis_name_pos = 'middle',yaxis_name_gap = 40,legend_pos='15%',label_color =['#003366','#3399CC','#CCCCCC','#99CCCC','#FFCC99','#FFFFCC'], is_stack=True)
# bar.render("./all_charts/"+"2.1每个人的出差天数统计"+".html")


group2 = []
sheet2 = pd.read_excel("./data_resources/2.3个人出差费用.xls")
people2 = sheet2["出差人"].values.tolist()
bar2 = Bar('个人出差费用排名')
for i in ["领导组", "硬件组", "销售组", "售前组", "大数据云计算组"]:
    group2.append((i, sheet2[i].values.tolist()))
for i in group2:
    bar2.add(i[0], people2, i[1],xaxis_rotate = 40, is_label_show = True, label_pos= 'inside',label_text_size=8,yaxis_name = '出差费用(万元)',yaxis_name_pos = 'middle',yaxis_name_gap = 40, is_legend_show = True, legend_pos='40%', is_stack=True)

bar2.render("./all_charts/"+"2.3个人出差费用"+".html")
# #
#
#
# sheet0 = pd.read_excel("./data_resources/个人出差人天成本比（补）.xlsx")
# people0 = sheet0["出差人"][0:10].values.tolist()
# days0 = sheet0["费用/天数"][0:10].values.tolist()
# bar0 = Bar('个人出差人天成本排名(前10名)',title_pos="60%")
# bar0.add('出差人',people0,days0,xaxis_rotate = 40, yaxis_name = '出差费用(元)',yaxis_name_pos = 'middle',yaxis_name_gap = 40,legend_pos="85%",label_text_size = 10, is_label_show = True, label_pos= 'inside',label_color =['#FFFFFF'],mark_point = ['max'])
# # bar.render(path = 'D:\\示例1.jpeg')
#
# # bar.render("./all_charts/"+"个人出差人天成本比（补）"+".html")
#
#
# # sheet1 = pd.read_excel("./data_resources/个人出差人天成本比（补）.xlsx")
# people1 = sheet0["出差人"][-10:].values.tolist()
# days1 = sheet0["费用/天数"][-10:].values.tolist()
# bar1 = Bar('个人出差人天成本排名(后10名)', title_top="50%", title_pos="60%")
# bar1.add('出差人',people1,days1,xaxis_rotate = 40, yaxis_name = '出差费用(元)',yaxis_name_pos = 'middle',yaxis_name_gap = 40,is_legend_show = False,legend_pos="85%",label_text_size = 10, is_label_show = True, label_pos= 'inside', mark_point = ['max'])
# # bar.render(path = 'D:\\示例1.jpeg')
#
#
#
# grid = Grid(height=720, width=1500)
# grid.add(bar, grid_bottom="60%", grid_right="55%")
# grid.add(bar2, grid_top="60%", grid_right="55%")
# grid.add(bar0, grid_bottom="60%", grid_left="55%")
# grid.add(bar1, grid_top="60%", grid_left="55%")
# grid.render("./all_charts/"+"2.1_2.3各人出差情况组合图"+".html")