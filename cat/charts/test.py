from pyecharts import  Bar, Grid

x = [
    "名字很长的x轴1",
    "名字很长的x轴2",
    "名字很长的x轴3",
    "名字很长的x轴4",
    "名字很长的x轴5",
    "名字很长的x轴6",
    "名字很长的x轴7",
    "名字很长的x轴8",
    "名字很长的x轴9",
]
y = [10, 20, 30, 40, 50, 60, 70, 80, 90]

grid = Grid()
bar = Bar("利用 Grid 解决 dataZoom 与 X 轴标签重叠问题")
bar.add("", x, y, is_datazoom_show=True, xaxis_interval=0, xaxis_rotate=30)
# 把 bar 加入到 grid 中，并适当调整 grid_bottom 参数，使 bar 图整体上移
grid.add(bar, grid_bottom="25%")
grid.render()