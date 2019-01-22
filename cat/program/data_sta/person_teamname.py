# coding=utf-8
import xlrd
import xlwt
import re
xls_file = xlrd.open_workbook("./result/前20个出差费用.xlsx")
table = xls_file.sheets()[0]
people_file =xlrd.open_workbook("18年每个人属于什么组.xlsx")
people_table = people_file.sheets()[0]
nrows = table.nrows
people_dict={}#每个人属于什么组，key是人名，value是组名
p_nrows = people_table.nrows
for rowx in range(1,p_nrows):
    data = people_table.row(rowx)
    people_dict[data[0].value] = data[1].value
print(nrows)
print(table.row(1))
print(people_dict)
print(table.row(0))

new_row = 0
workbook = xlwt.Workbook(encoding='utf8')#新建一个工作表格
worksheet = workbook.add_sheet(u'sheet1')
worksheet.write(new_row,new_row,"出差人")
worksheet.write(new_row,1,"售前组")
worksheet.write(new_row,2,"硬件组")
worksheet.write(new_row,3,"大数据云计算组")
worksheet.write(new_row,4,"软件组")
worksheet.write(new_row,5,"销售组")
worksheet.write(new_row,6,"领导组")
new_row+=1#行
col=0#列
data=table.row(new_row)
print(data)
print(people_dict[data[col].value])
print(data[1].value)
print(new_row)
for i in  range(1,nrows):
    data = table.row(i)
    teamname = people_dict[data[col].value]
    print(teamname)
    print(type(teamname))
    # if teamname == "售前组":
    #     worksheet.write(new_row, 1, data[1].value)
    #     continue
    # if teamname == "硬件组":
    #     worksheet.write(new_row, 2, data[1].value)
    #     continue
    # if  teamname == "大数据云计算组":
    #     worksheet.write(new_row, 3, data[1].value)
    #     continue
    # if teamname == "软件组":
    #     worksheet.write(new_row, 4, data[1].value)
    #     continue
    # if teamname == "销售组":
    #     worksheet.write(new_row, 5, data[1].value)
    #     continue
    # if teamname == "领导组":
    #     worksheet.write(new_row, 6, data[1].value)
    #     continue


workbook.save('person_team_money_out.xls')

