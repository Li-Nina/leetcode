#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

province_day = pd.read_excel("./resources/出差省天数.xls")
city_day = pd.read_excel("./resources/出差市天数.xls")

province_day_shouqian = pd.read_excel("./resources/售前出差省天数.xls")
city_day_shouqian = pd.read_excel("./resources/售前出差市天数.xls")
province_day_xiaoshou = pd.read_excel("./resources/销售出差省天数.xls")
city_day_xiaoshou = pd.read_excel("./resources/销售出差市天数.xls")
province_day_shouqian_xiaoshou = pd.read_excel("./resources/售前和销售出差省天数.xls")
city_day_shouqian_xiaoshou = pd.read_excel("./resources/售前和销售出差市天数.xls")

province_price = pd.read_excel("./resources/出差省成本.xls")
city_price = pd.read_excel("./resources/出差市成本.xls")

province_price_shouqian = pd.read_excel("./resources/售前出差省成本.xls")
city_price_shouqian = pd.read_excel("./resources/售前出差市成本.xls")
province_price_xiaoshou = pd.read_excel("./resources/销售出差省成本.xls")
city_price_xiaoshou = pd.read_excel("./resources/销售出差市成本.xls")
province_price_shouqian_xiaoshou = pd.read_excel("./resources/售前和销售出差省成本.xls")
city_price_shouqian_xiaoshou = pd.read_excel("./resources/售前和销售出差市成本.xls")


province_income = pd.read_excel("./resources/出差省合同（不包括北京）.xls")
city_income = pd.read_excel("./resources/出差市合同（不包括北京）.xls")

province_income_2018 = pd.read_excel("./resources/出差省合同_2018拓展落实项目统计_地图.xls")
# city_income_2018 = pd.read_excel("./resources/出差市合同（不包括北京）.xls")

province_efficiency = pd.read_excel("./resources/1.3出差省合同省成本比例（不包括北京）.xls")
city_efficiency = pd.read_excel("./resources/1.3出差城市与合同城市费用比值.xls")
#天数
province_day_data = list(zip(province_day["出差省"].values.tolist(), province_day["函数值"].values.tolist()))
city_day_data = list(zip(city_day["出差市"].values.tolist(), city_day["函数值"].values.tolist()))
# print("province_day_data:", province_day_data, sep='\n')
# print("city_day_data:", city_day_data, sep='\n')

province_day_data_shouqian = list(zip(province_day_shouqian["出差省"].values.tolist(), province_day_shouqian["函数值"].values.tolist()))
city_day_data_shouqian = list(zip(city_day_shouqian["出差市"].values.tolist(), city_day_shouqian["函数值"].values.tolist()))
province_day_data_xiaoshou = list(zip(province_day_xiaoshou["出差省"].values.tolist(), province_day_xiaoshou["函数值"].values.tolist()))
city_day_data_xiaoshou = list(zip(city_day_xiaoshou["出差市"].values.tolist(), city_day_xiaoshou["函数值"].values.tolist()))
province_day_data_shouqian_xiaoshou = list(zip(province_day_shouqian_xiaoshou["出差省"].values.tolist(), province_day_shouqian_xiaoshou["函数值"].values.tolist()))
city_day_data_shouqian_xiaoshou = list(zip(city_day_shouqian_xiaoshou["出差市"].values.tolist(), city_day_shouqian_xiaoshou["函数值"].values.tolist()))
print("province_day_data_shouqian_xiaoshou:", province_day_data_shouqian_xiaoshou, sep='\n')
print("city_day_data_shouqian_xiaoshou:", city_day_data_shouqian_xiaoshou, sep='\n')

#费用
province_price_data = list(zip(province_price["出差省"].values.tolist(), province_price["出差成本（万元）"].values.tolist()))
city_price_data = list(zip(city_price["出差市"].values.tolist(), city_price["出差成本（万元）"].values.tolist()))
# print("province_price_data:", province_price_data, sep='\n')
# print("city_price_data:", city_price_data, sep='\n')

province_price_data_shouqian = list(zip(province_price_shouqian["出差省"].values.tolist(), province_price_shouqian["出差成本（万元）"].values.tolist()))
city_price_data_shouqian = list(zip(city_price_shouqian["出差市"].values.tolist(), city_price_shouqian["出差成本（万元）"].values.tolist()))
province_price_data_xiaoshou = list(zip(province_price_xiaoshou["出差省"].values.tolist(), province_price_xiaoshou["出差成本（万元）"].values.tolist()))
city_price_data_xiaoshou = list(zip(city_price_xiaoshou["出差市"].values.tolist(), city_price_xiaoshou["出差成本（万元）"].values.tolist()))
province_price_data_shouqian_xiaoshou = list(zip(province_price_shouqian_xiaoshou["出差省"].values.tolist(), province_price_shouqian_xiaoshou["出差成本（万元）"].values.tolist()))
city_price_data_shouqian_xiaoshou = list(zip(city_price_shouqian_xiaoshou["出差市"].values.tolist(), city_price_shouqian_xiaoshou["出差成本（万元）"].values.tolist()))

#合同
province_income_data = list(zip(province_income["合同省"].values.tolist(), province_income["函数值"].values.tolist()))
city_income_data = list(zip(city_income["合同市"].values.tolist(), city_income["函数值"].values.tolist()))
# print("province_income_data:", province_income_data, sep='\n')
# print("city_income_data:", city_income_data, sep='\n')
province_income_data_2018 = list(zip(province_income_2018["合同省"].values.tolist(), province_income_2018["函数值"].values.tolist()))
#效费比
province_efficiency_data = list(zip(province_efficiency["合同省"][0:20].values.tolist(), province_efficiency["函数值"].values.tolist()))
city_efficiency_data = list(zip(city_efficiency["合同市"][0:17].values.tolist(), city_efficiency["函数值"].values.tolist()))
# print("province_efficiency_data:", province_efficiency_data, sep='\n')
# print("city_efficiency_data:", city_efficiency_data, sep='\n')


home_icon = 'image://data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAAnCAMAAAC7faEHAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAvVBMVEUAAAAfSH0fSHweSH0dSH0fSX0fSn8fR3sdSHsAP38fSHwfSX0fSXweSX0eSXwfSXweSXwfSXweSXwfR38eSHwfSHwfSX0fSXwfSH0fSX0fSHweSH0fSXwfSX0fSX0fSXweSXweSXwfSXweSX0gSX4fSH0fSXwfP38eSXweSH0gSHweSHwfSXweSX0eSX0bSH8fSXwfSXwfSH0fSXwfSHweSXwfSXweSX0fSX0fSXweSHwfRn4fSn0fSX3///+2E6yEAAAAPXRSTlMAguuGlPEwQDwE9ojx7+Lzj+jzIFT1gNX8q+7y9fby9Pv67PBv01AITNZ33+a/hBzl/qn5cff7z9X252H4LGPrQwAAAAFiS0dEPklkAOMAAAAJcEhZcwAAFxEAABcRAcom8z8AAAAHdElNRQfjAQUOBxeQtiQEAAABLUlEQVQ4y93RWUOCQBDA8RFB0TIRhJIOjyy6LDs0teb7f612hnNhF3nu/8Lu8nvYAYBKLaMNDTIttEzx7HRFdq+G9QmenA6oMz0bOkMBR8i5npaNYSwgoh8E5xoXMyB4gQbARO1SxhBDncsZw0tT7YqMoWWqnMxieFV1ZcbwuuKqLB6m5FSM4Y15nCXDSGyqYgJOC1Aw+vjKDMygYLMaN0sg3W1e4+bxHVs0glHjDBqmDQuatNbR1LewvLuH3EXdtCh38PD4VNhRz4O0l578Rtp5LqYlP0zrVgG1OuoCXgT/wXVe3xq59fukkfv4/NK60KPs+H4R3c/mk7DkNi63yebIDmSXlbos2fn8W53Cd3H4xC+57Te12+OBFwfc73ixldwa9Y0K7qevZb9LFn80o04DGKVQoQAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAxOS0wMS0wNVQyMTowNzoyMy0wNzowMJ/OgFQAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMTktMDEtMDVUMjE6MDc6MjMtMDc6MDDukzjoAAAAAElFTkSuQmCC'
