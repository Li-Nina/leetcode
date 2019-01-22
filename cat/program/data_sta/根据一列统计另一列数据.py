# coding=utf-8
import xlrd
import xlwt
xls_file = xlrd.open_workbook("./2018不包括北京/2018年1月.xlsx")
xls_sheet = xls_file.sheets()[0] #打开第几个bu
col_name= xls_sheet.col_values(19) #第7列为出差人
col_day= xls_sheet.col_values(10) #第11列为出差天数
del col_name[0]
print(col_name)
del col_day[0]
print(col_day)
print(len(col_name))
print(len(col_day))
num=len(col_name)
day_dict={}
for i in range(num):
   if col_name[i] in day_dict.keys():
        #print(dict[col_name[i]])
        day_dict[col_name[i]]= day_dict[col_name[i]] + col_day[i]
   else:
         day_dict[col_name[i]]= col_day[i]
print(day_dict)
#print (sorted(dict.items(), key=lambda d:d[1]))
#print(sorted(dict.items(), key=lambda d:d[1], reverse = True))
workbook = xlwt.Workbook(encoding='utf8')
worksheet = workbook.add_sheet(u'sheet1')
new_row=0
for k,v in day_dict.items():
    worksheet.write(new_row,0,k)
    worksheet.write(new_row,1,v)
    new_row+=1
workbook.save('./result/201801.xls')