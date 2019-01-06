import pyecharts.echarts.events as events
from pyecharts import Map, Geo
from pyecharts_javascripthon.dom import window
from math import ceil, floor, log10

from cat.map import data
from cat.map.data import home_icon


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
def generate(maptype, attr, value, folder_type):
    split_number = 5  # 分段的个数
    max_value = cal_proper_max_value(max(value), split_number)
    map = Map(maptype, width=1200, height=600)
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
        is_piecewise=True,  # 加上后组件为分段型
        visual_split_number=split_number,  # 分段的个数
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
    map.render("./maps/" + folder_type + "/" + maptype + '.html')


if __name__ == '__main__':
    province_name, province_value = Geo.cast(data.province_day_data)
    city_name, city_value = Geo.cast(data.city_day_data)
    generate('china', province_name, province_value, 'days')
    for province in province_name:
        generate(province, city_name, city_value, 'days')

    province_name, province_value = Geo.cast(data.province_price_data)
    city_name, city_value = Geo.cast(data.city_price_data)
    generate('china', province_name, province_value, 'prices')
    for province in province_name:
        generate(province, city_name, city_value, 'prices')
