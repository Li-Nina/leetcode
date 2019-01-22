# coding=utf-8
import xlrd
import xlwt
xls_file = xlrd.open_workbook("project_all (1).xlsx")
xls_sheet = xls_file.sheets()[0] #打开第几个bu
col_name= xls_sheet.col_values(1) #第2列单据编号
col_day= xls_sheet.col_values(10) #第11列为出差天数
del col_name[0]
print(col_name)
del col_day[0]
print(col_day)
print(len(col_name))
print(len(col_day))
num=len(col_name)
day_dict={}
chongfu_list=[]
for i in range(num):
   if col_name[i] in day_dict.keys():
        #print(dict[col_name[i]])
        #print("去重")
        #print(col_name[i])
        chongfu_list.append(col_name[i])
        day_dict[col_name[i]]= day_dict[col_name[i]] + col_day[i]
   else:
         day_dict[col_name[i]]= col_day[i]
print("###############")
print(chongfu_list)
print("@@@@@@@@@@@@@")
print("重复list的长度")
print(len(chongfu_list))

new_row = 0
workbook = xlwt.Workbook(encoding='utf8')
worksheet = workbook.add_sheet(u'sheet1')
data = xls_sheet.row(0)
col_num = len(data)
for i in range(col_num):
    worksheet.write(new_row,i,data[i].value) #单元格所在的row,column,和value.
new_row+=1
nrows = xls_sheet.nrows
#去重计数
quchong = 0
#从1行开始按照行遍历
for rowx in  range(1,nrows):
    data = xls_sheet.row(rowx)
    print("********")
    print(data[1].value)
    if data[1].value in chongfu_list:
        print("去重！！！！！！")
        quchong+=1
        chongfu_list.remove(data[1].value)
    else:
        for i in range(col_num):
            worksheet.write(new_row,i,data[i].value) #单元格所在的row,column,和value.
        new_row +=1
workbook.save('去重60个项目合并表.xls')
print("去重次数")
print(quchong)

