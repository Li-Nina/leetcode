from pyecharts import Geo

from cat.map import data

geo = Geo(
    "全国主要城市空气质量",
    "data from pm2.5",
    title_color="#fff",
    title_pos="center",
    width=1200,
    height=600,
    background_color="#404a59",
)
attr, value = geo.cast(data.city_data)
geo.add(
    "",
    attr,
    value,
    # type="heatmap",
    type="scatter",
    # maptype="广东",
    # type="effectScatter",
    visual_range=[0, 1000],
    visual_text_color="#fff",
    symbol_size=15,
    is_visualmap=True,
)
geo.render()
