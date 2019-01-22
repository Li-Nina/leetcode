from pyecharts import Bar,Grid
import pandas as pd

sheet0 = pd.read_excel("./data_resources/出差省合同省成本比.xls")
people0 = sheet0["合同省"][0:10].values.tolist()
days0 = sheet0["合同/出差"][0:10].values.tolist()
bar0 = Bar('出差地区与合同效费比',title_pos="10%")
bar0.add('合同省',people0,days0,xaxis_rotate = 40, yaxis_name = '合同/出差（%）',yaxis_name_pos = 'middle',yaxis_name_gap = 40,legend_pos="35%",label_text_size = 12, is_label_show = True)
# bar.render(path = 'D:\\示例1.jpeg')

# bar.render("./all_charts/"+"个人出差人天成本比（补）"+".html")


# sheet1 = pd.read_excel("./data_resources/1.3出差城市与合同城市费用比值.xls")
# people1 = sheet1["合同市"][0:10].values.tolist()
# days1 = sheet1["合同/出差"][0:10].values.tolist()
# bar1 = Bar('出差城市与合同城市费用比值',title_pos="55%")
# bar1.add('合同市',people1,days1,xaxis_rotate = 40, yaxis_name = '成本比例（%）',yaxis_name_pos = 'middle',yaxis_name_gap = 40,legend_pos="80%",label_text_size = 8, is_label_show = True, label_pos= 'inside',mark_point = ['max'])
# # bar.render(path = 'D:\\示例1.jpeg')
grid = Grid(width=850)
grid.add(bar0, grid_right="20%")
# grid = Grid(width=1200)
# grid.add(bar0, grid_right="55%")
# # grid.render("./all_charts/"+"各组出差天数费用0.xls"+".html")
# grid.add(bar1, grid_left="50%")
grid.render("./all_charts/"+"1.3出差地区与合同效费比"+".html")