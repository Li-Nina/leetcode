import pyecharts.echarts.events as events
from pyecharts import Map, Bar, Geo, Grid
from pyecharts_javascripthon.dom import window
from math import ceil, floor, log10

from cat.map import data
from cat.map.data import home_icon
import pandas as pd


def on_click(event):
    if event.name in ['安徽', '北京', '福建', '甘肃', '广东', '广西', '贵州', '海南', '河北', '河南', '黑龙江', '湖北', '湖南',
                      '江苏', '江西', '辽宁', '内蒙古', '宁夏', '山东', '山西', '陕西', '上海', '四川', '天津', '西藏', '新疆',
                      '云南', '浙江', '重庆', '青海', '吉林', '台湾']:
        window.open(event.name + '.html', '_self')


def format(w):
    if w.name:
        return w.name + ':' + w.value
    else:
        return 0


def return_home():
    window.open('china.html', '_self')


# def label_format(w):
#     return w.name + ':' + w.value


def cal_proper_max_value(max_value, split_number):
    if max_value < 1:
        return max_value
    interval = ceil(max_value / split_number)
    extend_interval = pow(10, floor(log10(interval)))
    interval = extend_interval * ceil(interval / extend_interval)
    max_value = interval * split_number
    return max_value


# 1200*600
def generate1(maptype, attr, value, folder_type, label_name):
    split_number = 5  # 分段的个数
    max_value = cal_proper_max_value(max(value), split_number)
    map = Map(maptype, width=800, height=500, title_pos="10%")
    map.add(
        "",
        attr,
        value,
        maptype=maptype,
        is_roam=True,
        is_label_show=True,
        is_map_symbol_show=False,
        is_visualmap=True,
        visual_range=[0, max_value],  # 最大值必须要大于真实的数值
        visual_text_color="#000",
        visual_range_color=['#CCFFFF', '#99CCFF', '#336699', '# 003366'],
        visual_range_text=[' ', '单位(人天数)'],
        # is_piecewise=True,  # 加上后组件为分段型
        # visual_split_number=split_number,  # 分段的个数
        tooltip_formatter=format,
        # label_formatter=label_format, #地图上省份直接显示数据
    )
    # map.use_theme("shine")
    map._option.get("toolbox").get("feature").update(
        {
            "myTool": {"show": True, "title": "返回全国地图", "icon": home_icon, "onclick": return_home},
        }
    )
    map.on(events.MOUSE_CLICK, on_click)
    # map.render("./maps" + "ggggg人天数组合图" + ".html")

    map.render("./maps/" + folder_type + "/" + maptype + '.html')


if __name__ == '__main__':
    grid = Grid(width=1400, height=600)
    province_name, province_value = Geo.cast(data.province_day_data)
    city_name, city_value = Geo.cast(data.city_day_data)

    bar = Bar('各地出差人天数排名柱状图', title_pos="65%")
    bar.add('出差人', province_name[0:10], province_value[0:10], xaxis_rotate=40, yaxis_name='出差数(天)',
            yaxis_name_pos='middle', is_roam=True,
            yaxis_name_gap=40, is_label_show=True, legend_pos="86%", legend_orient="vertical", mark_point=['max'])

    split_number = 5  # 分段的个数
    max_value = cal_proper_max_value(max(province_value), split_number)
    map = Map('china', width=70, height=60, title_pos="10%")
    map.add(
        "",
        province_name,
        province_value,
        maptype='china',
        is_roam=True,
        is_label_show=True,
        is_map_symbol_show=False,
        # tooltip_formatter=format,
        is_visualmap=True,
        # left = '1',
        visual_range=[0, max_value],
        visual_text_color="#000",
        visual_range_color=['#CCFFFF', '#99CCFF', '#336699', '# 003366'],
        visual_range_text=[' ', '单位(人天数)'],
        # is_piecewise=True,  # 加上后组件为分段型
        # visual_split_number=split_number,  # 分段的个数
        # label_formatter=label_format, #地图上省份直接显示数据
    )
    grid.on(events.MOUSE_CLICK, on_click)
    # map.use_theme("shine")

    # map._option.update({"layoutCenter": ['30%', '30%']})

    # map.render("./maps" + "ggggg人天数组合图" + ".html")
    grid.add(bar, grid_left='60%')
    grid.add(map, grid_right='left',grid_bottom='20%')
    grid._option.get("toolbox").get("feature").update(
        {
            "myTool": {"show": True, "title": "返回全国地图", "icon": home_icon, "onclick": return_home},
        }
    )

    print("-----------------------------------------------------------------bar")
    bar.print_echarts_options()
    print("-----------------------------------------------------------------map")
    map.print_echarts_options()
    # grid._option.pop("visualMap")

    map._option.get("visualMap", {}).update({"seriesIndex": 1})

    grid._option.update({
        "visualMap": [
            bar._option.get("visualMap", {"seriesIndex": 0, "show": False}),
            map._option.get("visualMap"),
        ],
    })
    #
    # series = grid._option.get("series")

    grid._option.get("tooltip")._config.update({"formatter": format})

    # bar._option.get("tooltip")._config.update({"confine": True})
    # map._option.get("tooltip")._config.update({"confine": True})
    #
    # series[0]['tooltip'] = bar._option.get("tooltip")._config
    # series[1]['tooltip'] = map._option.get("tooltip")._config

    # grid._option.pop("tooltip")

    grid.render("./maps/" + 'days' + "/" + 'china' + '.html')

    print("-----------------------------------------------------------------grid")
    grid.show_config()

    # for province in province_name:
    #     generate1(province, city_name, city_value, 'days', '单位(人天数)')

    # province_name, province_value = Geo.cast(data.province_price_data)
    # city_name, city_value = Geo.cast(data.city_price_data)
    # generate('china', province_name, province_value, 'prices','单位(万元)')
    # for province in province_name:
    #     generate(province, city_name, city_value, 'prices','单位(万元)')
