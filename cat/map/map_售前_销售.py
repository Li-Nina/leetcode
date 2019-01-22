import pyecharts.echarts.events as events
from pyecharts import Map, Geo
from pyecharts_javascripthon.dom import window
from math import ceil, floor, log10, log, pow

from cat.map import data
from cat.map.data import home_icon
from decimal import Decimal


def on_click(event):
    if event.name in ['安徽', '北京', '福建', '甘肃', '广东', '广西', '贵州', '海南', '河北', '河南', '黑龙江', '湖北', '湖南',
                      '江苏', '江西', '辽宁', '内蒙古', '宁夏', '山东', '山西', '陕西', '上海', '四川', '天津', '西藏', '新疆',
                      '云南', '浙江', '重庆', '青海', '吉林', '台湾']:
        window.open(event.name + '.html', '_self')


def format_1(w):
    # aa = (pow(w.value/937.5, 2.5) * 937.5).toFixed(2)
    if w.name:
        aa = ((w.value / 245.63)**2.5 * 245.63).toFixed(2)
        # aa = (pow(w.value/937.5, 2.5) * 937.5).toFixed(2)
        return w.name + ':' + aa
    # else:
    #     return 0
def format_2(w):
    # bb = pow(w.value/353265.3333,1/0.6)*353265.3333
    # print(22222222222222222222)
    print(w.name)
    if w.name:
        # bb = ((w.value / 353265.333)**(1/0.6) * 353265.3333).toFixed(2)
        return w.name + ':' + w.value

def return_home():
    window.open('china.html', '_self')


# def label_format(w):
#     return w.name + ':' + w.value

# def log_value(old_value):
#     new_value = []
#     for i in old_value:
#         if i is not None:
#             new_value.append(log10(i))
#     return new_value

def cal_proper_max_value(max_value, split_number):
    if max_value < 1:
        return max_value
    interval = ceil(max_value / split_number)
    extend_interval = pow(10, floor(log10(interval)))
    # extend_interval = pow(10, floor(log(interval,20)))
    interval = extend_interval * ceil(interval / extend_interval)
    max_value = interval * split_number
    return max_value


# 1200*600
def generate(map_name, maptype, attr, value, folder_type, label_name):
    split_number = 5  # 分段的个数
    max_value = cal_proper_max_value(max(value), split_number)
    map = Map(map_name, width=1000, height=600)
    if folder_type == 'days_shouqian' or folder_type == 'days_xiaoshou' or folder_type == 'days_shouqian_xiaoshou':
        map.add(
            "",
            attr,
            value,
            maptype=maptype,
            is_roam='move',
            # is_roam = True,
            is_label_show=True,
            is_map_symbol_show=False,
            is_visualmap=True,
            visual_range=[0, max_value],  # 最大值必须要大于真实的数值
            visual_text_color="#000",
            visual_range_color=['#63BE7B', '#83C77D', '#A2D07F', '#C1DA81', '#E0E383', '#FFEB84', '#FDD17F', '#FCB77A', '#FA9D75', '#F98370', '#F8696B'],

            # visual_range_color=['#F8696B', '#F98370', '#FA9D75', '#FCB77A', '#FDD17F', '#FFEB84', '#E0E383', '#C1DA81', '#A2D07F', '#83C77D', '#63BE7B'],
            # visual_text_color="#FF0000",
            # visual_range_color=['#5BC39E', '#FFB64B', '#FB806E'],
            # visual_range_color=['#CCFFFF', '#99CCFF', '#336699', '# 003366'],#纯色渐变
            # visual_range_color=['#2DC3DE', '#48B4D0', '#2EBFC4', '#2AB29C', '#3CA57D', '#42946E', '#577E52', '#BB4543',
            #                     '#D23B42'],#keep色
            visual_range_text=[' ', label_name],
            # is_piecewise=True,  # 加上后组件为分段型
            # visual_split_number=split_number,  # 分段的个数
            tooltip_formatter=format_1,
            # label_formatter=label_format, #地图上省份直接显示数据
        )
    elif folder_type == 'price_shouqian' or folder_type == 'price_xiaoshou' or folder_type == 'price_shouqian_xiaoshou':
        map.add(
            "",
            attr,
            value,
            maptype=maptype,
            is_roam='move',
            is_label_show=True,
            is_map_symbol_show=False,
            is_visualmap=True,
            visual_range=[0, max_value],  # 最大值必须要大于真实的数值
            visual_text_color="#000",
            visual_range_color=['#63BE7B', '#83C77D', '#A2D07F', '#C1DA81', '#E0E383', '#FFEB84', '#FDD17F', '#FCB77A', '#FA9D75', '#F98370', '#F8696B'],

            # visual_range_color=['#F8696B', '#F98370', '#FA9D75', '#FCB77A', '#FDD17F', '#FFEB84', '#E0E383', '#C1DA81', '#A2D07F', '#83C77D', '#63BE7B'],
            # visual_text_color="#FF0000",
            # visual_range_color=['#5BC39E', '#FFB64B', '#FB806E'],
            # visual_range_color=['#CCFFFF', '#99CCFF', '#336699', '# 003366'],#纯色渐变
            # visual_range_color=['#2DC3DE', '#48B4D0', '#2EBFC4', '#2AB29C', '#3CA57D', '#42946E', '#577E52', '#BB4543',
            #                     '#D23B42'],#keep色
            visual_range_text=[' ', label_name],
            # is_piecewise=True,  # 加上后组件为分段型
            # visual_split_number=split_number,  # 分段的个数
            tooltip_formatter=format_2,
            # label_formatter=label_format, #地图上省份直接显示数据
        )
    # map.use_theme("shine")
    map._option.get("toolbox").get("feature").update(
        {
            "myTool": {"show": True, "title": "home", "icon": home_icon, "onclick": return_home},
        }
    )
    map.on(events.MOUSE_CLICK, on_click)
    map.render("./maps/" + folder_type + "/" + maptype + '.html')


if __name__ == '__main__':
#天数
    province_name_shouqian, province_value_shouqian = Geo.cast(data.province_day_data_shouqian)
    city_name_shouqian, city_value_shouqian = Geo.cast(data.city_day_data_shouqian)
    generate('售前组出差人天数地域分布图', 'china', province_name_shouqian, province_value_shouqian, 'days_shouqian', '单位(人天数)')
    for province in province_name_shouqian:
        generate('售前组出差人天数地域分布图', province, city_name_shouqian, city_value_shouqian, 'days_shouqian', '单位(人天数)')

    province_name_xiaoshou, province_value_xiaoshou = Geo.cast(data.province_day_data_xiaoshou)
    city_name_xiaoshou, city_value_xiaoshou = Geo.cast(data.city_day_data_xiaoshou)
    generate('销售组出差人天数地域分布图', 'china', province_name_xiaoshou, province_value_xiaoshou, 'days_xiaoshou', '单位(人天数)')
    for province in province_name_xiaoshou:
        generate('销售组出差人天数地域分布图', province, city_name_xiaoshou, city_value_xiaoshou, 'days_xiaoshou', '单位(人天数)')

    province_name_shouqian_xiaoshou, province_value_shouqian_xiaoshou = Geo.cast(data.province_day_data_shouqian_xiaoshou)
    city_name_shouqian_xiaoshou, city_value_shouqian_xiaoshou = Geo.cast(data.city_day_data_shouqian_xiaoshou)
    generate('售前组和销售组出差人天数地域分布图', 'china', province_name_shouqian_xiaoshou, province_value_shouqian_xiaoshou, 'days_shouqian_xiaoshou', '单位(人天数)')
    for province in province_name_shouqian_xiaoshou:
        generate('售前组和销售组出差人天数地域分布图', province, city_name_shouqian_xiaoshou, city_value_shouqian_xiaoshou, 'days_shouqian_xiaoshou', '单位(人天数)')
#费用
    province_name_shouqian, province_value_shouqian = Geo.cast(data.province_price_data_shouqian)
    city_name_shouqian, city_value_shouqian = Geo.cast(data.city_price_data_shouqian)
    generate('售前组出差费用地域分布图', 'china', province_name_shouqian, province_value_shouqian, 'price_shouqian', '单位(万元)')
    for province in province_name_shouqian:
        generate('售前组出差费用地域分布图', province, city_name_shouqian, city_value_shouqian, 'price_shouqian', '单位(万元)')

    province_name_xiaoshou, province_value_xiaoshou = Geo.cast(data.province_price_data_xiaoshou)
    city_name_xiaoshou, city_value_xiaoshou = Geo.cast(data.city_price_data_xiaoshou)
    generate('销售组出差费用地域分布图', 'china', province_name_xiaoshou, province_value_xiaoshou, 'price_xiaoshou', '单位(万元)')
    for province in province_name_shouqian:
        generate('销售组出差费用地域分布图', province, city_name_xiaoshou, city_value_xiaoshou, 'price_xiaoshou', '单位(万元)')

    province_name_shouqian_xiaoshou, province_value_shouqian_xiaoshou = Geo.cast(data.province_price_data_shouqian_xiaoshou)
    city_name_shouqian_xiaoshou, city_value_shouqian_xiaoshou = Geo.cast(data.city_price_data_shouqian_xiaoshou)
    generate('售前组和销售组出差费用地域分布图', 'china', province_name_shouqian_xiaoshou, province_value_shouqian_xiaoshou, 'price_shouqian_xiaoshou', '单位(万元)')
    for province in province_name_shouqian:
        generate('售前组和销售组出差费用地域分布图', province, city_name_shouqian_xiaoshou, city_value_shouqian_xiaoshou, 'price_shouqian_xiaoshou', '单位(万元)')
