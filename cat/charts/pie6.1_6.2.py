from pyecharts import Pie,Bar, Grid
import pandas as pd

# sheet0 = pd.read_excel("./data_resources/6.1去重全事业部各个支出类型费用占比.xls")
# group0 = sheet0["单据类型"].values.tolist()
# days0 = sheet0["金额（万元）"].values.tolist()
# pie0 = Pie('全事业部中各种支付类型的金额',title_pos="0%")
# pie0.add('项目费用类别',group0,days0, radius=[45, 65],center=[40, 50],is_label_show = True, legend_orient = 'vertical',legend_pos="80%",label_text_size = 10,mark_point = ['max'])
# grid = Grid(width=800,height=400)
# grid.add(pie0, grid_right="10%")
# # grid.render("./all_charts/"+"各组出差天数费用0.xls"+".html")
# grid.render("./all_charts/"+"6.1全事业部各个支出类型费用占比"+".html")

# sheet1 = pd.read_excel("./data_resources/6.2去重全事业部各项目支出占比.xls")
# group1 = sheet1["项目名称"][0:10].values.tolist()
# days1 = sheet1["项目金额（万元）"][0:10].values.tolist()
# pie1 = Pie('全事业部中各个项目支出的占比',title_pos="35%")
# pie1.add('项目名称',group1,days1, radius=[45, 65],center=[40, 50],is_label_show = False,legend_orient = 'vertical',legend_pos="60%",label_text_size = 10,mark_point = ['max'])
# # bar.render(path = 'D:\\示例1.jpeg')

# sheet1 = pd.read_excel("./data_resources/6.2去重全事业部各项目支出占比_20.xls")
# group1 = sheet1["简称"].values.tolist()
# days1 = sheet1["金额（万元取整）"].values.tolist()
# pie1 = Pie('全事业部中各个项目支出的占比',title_pos="0%")
# pie1.add('项目名称',group1,days1, radius=[45, 65],center=[40, 50],is_label_show = False,legend_orient = 'vertical',legend_pos="60%",label_text_size = 10,mark_point = ['max'])
# # bar.render(path = 'D:\\示例1.jpeg')

sheet1 = pd.read_excel("./data_resources/6.2去重全事业部各项目支出占比_10.xls")
group1 = sheet1["简称"][0:10].values.tolist()
days1 = sheet1["金额（万元取整）"][0:10].values.tolist()
bar0 = Bar('全事业部中各个项目支出', title_pos="0%")
bar0.add('项目名称', group1,days1,height=0, xaxis_rotate =50, xaxis_label_textsize=12,yaxis_name = '项目支出(万元)',yaxis_name_pos = 'middle',yaxis_name_gap = 40,legend_pos="25%", is_label_show = True)
# bar0.add('项目名称', group0, days0, height=0, xaxis_rotate =40, xaxis_label_textsize=12,yaxis_name = '出差费用(万元)',yaxis_name_pos = 'middle',yaxis_name_gap = 40,legend_pos="25%",label_text_size=10, is_label_show = True)
# bar0.render("./all_charts/"+"6.2去重全事业部各项目支出柱状图"+".html")

# bar.render(path = 'D:\\示例1.jpeg')
#
#
grid = Grid(width=800,height=400)
# grid.add(pie0, grid_right="50%")
# grid.render("./all_charts/"+"各组出差天数费用0.xls"+".html")
grid.add(bar0, grid_right="10%",grid_bottom= "20%")
grid.render("./all_charts/"+"6.2去重全事业部各项目支出柱状图"+".html")
