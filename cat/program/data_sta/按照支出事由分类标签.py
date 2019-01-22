# coding=utf-8
import xlrd
import xlwt
import chardet
import re
import jieba
import jieba.posseg as psg
xls_file = xlrd.open_workbook("merge_project_all.xlsx")

# （1）办公：快递、通讯费、运输、交通
# （2）会议：会议、评审
# （3）差旅
# （4）图书资料
# （5）餐费：加班餐、招待餐
# （6）知识产权：印刷、版面、制作、查新、专利、打印
# （7）外协费
# （8）材料费
# （9）试验费
#  （10）实习劳务费
meeting_list =["峰会","会议","论坛","评审","大会","参会","评审会","会议费","高层论坛","协会","举办会","展会","展会服务","参展费","展位费","参展","展位"]
book_list=["图书","资料"]
office_list=["交通费","交通","运输","通讯","快递","快递费","物流费","物流","租车费","租车","货运费","货运","打车费","打车"]
patent_list=["专利","印刷","版面","制作","查新","专利费","软件著作","著作权","专利申请"]
receipt_list=["外协","材料","试验","材料费","版面","印刷","制作","制作费","版面费"]
know_list=["版面","印刷","制作","制作费","版面费","打印费","打印"]
test_list=["测试","实验"]
intern_list=["实习","实习生"]
teach_list=["培训","培训费"]
out_list=["差旅"]
table = xls_file.sheets()[0]#打开第几个bu
# people_file =xlrd.open_workbook("组名.xlsx")
# people_table = people_file.sheets()[0]
nrows = table.nrows

# people_dict={}
# p_nrows = people_table.nrows
# for rowx in range(1,p_nrows):
#     data = people_table.row(rowx)
#     people_dict[data[0].value] = data[1].value
print(nrows)#table的行数
print(table.row(0))#table的第一行表头
print(table.row(1))#table的第二行

new_row = 0
workbook = xlwt.Workbook(encoding='utf8')
worksheet = workbook.add_sheet(u'sheet1')
data = table.row(0)
col_num = len(data)
for i in range(col_num):
    worksheet.write(new_row,i,data[i].value) #单元格所在的row,column,和value.
worksheet.write(new_row,col_num,"单据类型说明")
new_row+=1
name_dict={}
#从1行开始按照行遍历
for rowx in  range(1,nrows):
    data = table.row(rowx)
    event = data[2].value
    old_type = data[3].value
    status =  data[5].value
    receipt_type = data[9].value
    print(event)  # 要分词的事件类型
    # # seg_list = psg.lcut(event)
    # # print(seg_list)  # 分词结果词seg.word,分词类型seg.flag
    # # event_word_num = len(seg_list)
    # # print(event_word_num)
    #old_type=old_type.encode('utf-8')
    if (status == "被退回" ):
        new_row += 1
        continue
    if (old_type == u'差旅'):
        for i in range(col_num):
            worksheet.write(new_row,i,data[i].value) #单元格所在的row,column,和value.
        worksheet.write(new_row,col_num,old_type)
        new_row +=1
        continue

    for seg in psg.lcut(event):
        if seg.word in meeting_list:
            print(seg.word)
            new_type = "会议"
            break
        elif seg.word in book_list:
            print(seg.word)
            new_type = "图书资料"
            break
        elif seg.word in office_list:
            print(seg.word)
            new_type = "办公费"
            break
        elif seg.word in patent_list:
            print(seg.word)
            new_type = "知识产权"
            break
        elif seg.word in test_list:
            print(seg.word)
            new_type = "试验费"
            break
        elif seg.word in intern_list:
            print(seg.word)
            new_type = "实习劳务费"
            break
        elif seg.word in teach_list:
            print(seg.word)
            new_type = "培训费"
            break
        else:
            print(seg.word)
            new_type = old_type
    for seg in psg.lcut(receipt_type):
        if seg.word in receipt_list:
            print(seg.word)
            new_type = receipt_type
            break
    for seg in psg.lcut(receipt_type):
        if seg.word in know_list:
            print(seg.word)
            new_type = "知识产权"
            break
    for seg in psg.lcut(old_type):
        if seg.word in out_list:
            print(seg.word)
            new_type = old_type
            break
    for i in range(col_num):
        worksheet.write(new_row, i, data[i].value)  # 单元格所在的row,column,和value.
    worksheet.write(new_row, col_num, new_type)
    new_row += 1
workbook.save('merge_project_out.xls')