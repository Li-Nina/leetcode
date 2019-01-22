from pyecharts import Pie,Grid
import pandas as pd

sheet = pd.read_excel("./data_resources/3.3每个组的出差天数除以每个组的总人数.xls")
group0 = sheet["组名"].values.tolist()
days0 = sheet["总人数"].values.tolist()
pie0 = Pie('各组人数比例',title_pos="10%")
pie0.add('组名',group0,days0, radius=[45, 65],center=[20, 50],is_label_show = True, legend_orient = 'vertical',legend_pos="40%",label_text_size = 10,mark_point = ['max'])
# bar.render(path = 'D:\\示例1.jpeg')

group1 = sheet["组名"].values.tolist()
days1 = sheet["出差天数/总人数"].values.tolist()
pie1 = Pie('各组人员出差人天数密度',title_pos="55%")
pie1.add('组名',group1,days1, radius=[45, 65],center=[65, 50],is_label_show = True,legend_orient = 'vertical',legend_pos="85%",label_text_size = 10,mark_point = ['max'])
# bar.render(path = 'D:\\示例1.jpeg')


grid = Grid(width=1200)
grid.add(pie0, grid_right="55%")
# grid.render("./all_charts/"+"各组出差天数费用0.xls"+".html")
grid.add(pie1, grid_left="50%")
grid.render("./all_charts/"+"3.1_3.3每个组的出差人天数密度"+".html")