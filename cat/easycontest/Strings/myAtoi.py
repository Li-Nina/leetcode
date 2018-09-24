import re


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # str_list = []
        # for i in str.lstrip():
        #     if not str_list and (i == '-' or i == '+'):
        #         str_list.append(i)
        #     elif i.isdigit():
        #         str_list.append(i)
        #     else:
        #         break
        # if str_list and not (len(str_list)==1 and not str_list[0].isdigit()):
        #     if -2 ** 31 <= int(''.join(str_list)) <= 2 ** 31 - 1:
        #         return int(''.join(str_list))
        #     elif int(''.join(str_list)) > 2 ** 31 - 1:
        #         return 2 ** 31 - 1
        #     else:
        #         return -2 ** 31
        # else:
        #     return 0
        # 正则表达式
        m = re.match("\s*([-|+]?[\d]+).*", str)  # .表示任意字符，*表示零个或多个，只有添加了才能匹配成功
        print(m)
        if not m:
            return 0
        else:
            x = int(m.group(1))  # ()用于分组，1表示取第一个括号里的匹配项
            if x < -2 ** 31:
                return -2 ** 31
            elif x > 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return x


a = " +2345]"
print(Solution().myAtoi(a))
#         m = re.match("\s*([+]?[\d]+]).*", str)  # .表示任意字符，*表示零个或多个，只有添加了才能匹配成功

# str="    2345ert"
# m = re.match("\s*([+|-]?[\d]+).*", str)  # .表示任意字符，*表示零个或多个，只有添加了才能匹配成功
# print(m)
# a = ['1', '2', '3']
# print(int(''.join(a)))
