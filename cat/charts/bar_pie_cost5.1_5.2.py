from pyecharts import Bar, Pie, Grid
import pandas as pd

sheet1 = pd.read_excel("./data_resources/5.2各个项目出差费用占项目费用和的比（含北京）.xls")
group1 = sheet1["项目名称1"][0:7].values.tolist()
days1 = sheet1["出差占项目的比值"][0:7].values.tolist()
bar1 = Bar('各项目出差费用占项目经费比例',title_pos="0%")
bar1.add('项目名称', group1, days1, height=0, xaxis_rotate =40, xaxis_label_textsize=12,yaxis_name = '出差费用/项目经费(%)',yaxis_name_pos = 'middle',yaxis_name_gap = 40,legend_pos="40%",is_label_show = True)

bar1.render("./all_charts/"+"5.2各项目出差费用占项目经费比例"+".html")
#
# sheet0 = pd.read_excel("./data_resources/5.1各个项目出差费用柱状图（含北京）.xls")
# group0 = sheet0["项目名称1"][0:8].values.tolist()
# days0 = sheet0["出差费用（四舍五入取整）"][0:8].values.tolist()
# bar0 = Bar('各项目出差费用排名', title_pos="0%")
# bar0.add('项目名称', group0, days0, height=0, xaxis_rotate =50, xaxis_label_textsize=12,yaxis_name = '出差费用(万元)',yaxis_name_pos = 'middle',yaxis_name_gap = 40,legend_pos="25%", is_label_show = True)
# # bar0.add('项目名称', group0, days0, height=0, xaxis_rotate =40, xaxis_label_textsize=12,yaxis_name = '出差费用(万元)',yaxis_name_pos = 'middle',yaxis_name_gap = 40,legend_pos="25%", is_label_show = True)
# bar0.render("./all_charts/"+"5.1各项目出差费用柱状图"+".html")

# sheet0 = pd.read_excel("./data_resources/5.1各个项目出差费用饼图（含北京）.xls")
# group0 = sheet0["项目名称1"][0:8].values.tolist()
# days0 = sheet0["出差费用（四舍五入取整）"][0:8].values.tolist()
# pie0 = Pie("各项目出差费用排名", title_pos="0%")
# pie0.add('项目名称',group0,days0,radius=[45, 65],center=[45, 55],is_label_show = True,legend_pos="70%",legend_orient="vertical")
# # bar0.add('项目名称', group0, days0, height=0, xaxis_rotate =40, xaxis_label_textsize=12,yaxis_name = '出差费用(万元)',yaxis_name_pos = 'middle',yaxis_name_gap = 40,legend_pos="25%", is_label_show = True)
# pie0.render("./all_charts/"+"5.1各项目出差费用饼状图"+".html")
#
# sheet1 = pd.read_excel("./data_resources/5.2各个项目出差费用+项目经费.xls")
# group1 = sheet1["项目名称"][0:7].values.tolist()
# days1 = sheet1["出差占项目的比值"][0:7].values.tolist()
# pie1 = Pie('各项目出差费用占项目经费比例',title_pos="38%")
# pie1.add('项目名称',group1,days1,radius=[45, 65],center=[60, 55],is_label_show = True,legend_pos="70%",legend_orient="vertical",mark_point = ['max'])
#
#
# # 把 bar 加入到 grid 中，并适当调整 grid_bottom 参数，使 bar 图整体上移
# grid = Grid(width=1400)
# grid.add(bar0, grid_right="65%",grid_bottom="25%")
# # # grid.render("./all_charts/"+"各组出差天数费用0.xls"+".html")
# grid.add(pie1, grid_left="30%",grid_bottom="25%")
# grid.render("./all_charts/"+"5.1_5.2各项目出差费用组合图"+".html")