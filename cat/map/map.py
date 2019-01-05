import pyecharts.echarts.events as events
from pyecharts import Map, Geo
from pyecharts_javascripthon.dom import window

from cat.map import data


def on_click(event):
    if event.name in ['安徽', '北京', '福建', '甘肃', '广东', '广西', '贵州', '海南', '河北', '河南', '黑龙江', '湖北', '湖南',
                      '江苏', '江西', '辽宁', '内蒙古', '宁夏', '山东', '山西', '陕西', '上海', '四川', '天津', '西藏', '新疆',
                      '云南', '浙江', '重庆', '青海', '吉林', '台湾']:
        window.open(event.name + '.html')


def format(w):
    if w.name:
        return w.name + ':' + w.value
    else:
        return 0


# def lable_format(w):
#     return w.name + ':' + w.value

def generate(maptype, attr, value):
    map = Map(maptype, width=1200, height=600)
    map.add(
        "",
        attr,
        value,
        maptype=maptype,
        # maptype="china",
        # maptype="内蒙古",
        is_roam=True,
        is_label_show=True,
        is_map_symbol_show=False,
        is_visualmap=True,
        visual_range=[0, 1000],  # 最大值必须要大于真实的数值
        visual_text_color="#000",
        is_piecewise=True,
        visual_split_number=5,  # 分割的个数
        tooltip_formatter=format,
        # label_formatter=lable_format, #地图上省份直接显示数据
    )
    map.on(events.MOUSE_CLICK, on_click)
    map.render("./maps/" + maptype + '.html')


if __name__ == '__main__':
    province_name, province_value = Geo.cast(data.province_data)
    city_name, city_value = Geo.cast(data.city_data)
    generate('china', province_name, province_value)
    for province in province_name:
        generate(province, city_name, city_value)
