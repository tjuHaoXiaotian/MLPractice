# coding=utf-8

# 六种内建序列： list、元组、字符串、u 字符串、

greeting = "hello"
print greeting[0]

print greeting[-1]

# # 根据给定的年月日，以数字形式打印出日期
# months = [
#     'january',
#     'february',
#     'march',
#     'april',
#     'may',
#     'june',
#     'july',
#     'august',
#     'september',
#     'october',
#     'november',
#     'december'
# ]
#
# # 以1~31的数字作为结尾的列表
# endings = ['st','nd','rd'] + 17 * ['th'] \
#     + ['st','nd','rd'] + 7 * ['th'] \
#     +['st']
# year = raw_input("Year:")
# # help(raw_input)
# month = raw_input("Month (1-12): ")
# day = raw_input("Day (1-31): ")
#
# month_number = int(month)
# day_number = int(day)
#
# month_name = months[month_number-1]
# ordinal = day + endings[day_number-1]
#
# print month_name + ' ' + ordinal + ',' + year

# 分片，左开右闭
numbers = [1,2,3,4,5,6,7,8,9,10]
print numbers

print numbers[2:3]
print numbers[-4:-2]
print numbers[-4:]

print numbers[:5]
print numbers[1::2]

print [1,2,3]+[3,2,1]

print 3 * [1,2,3]

# 盒子内部居中打印
sentence = raw_input("Sentence")

txt_width = len(sentence)
margin_left = 6
margin_right = 6
inner_width = (margin_left + txt_width + margin_right)
print
print '+' + '-'*inner_width + '+'
print '|' + ' '*inner_width + '|'
print '|' + ' '*margin_left + sentence + ' '*margin_right + '|'
print '|' + ' '*inner_width + '|'
print '+' + '-'*inner_width + '+'

print ('haoxiaotian' in sentence)

# 列表与元组的区别

# 1: del
names = ["a","b","c"]
print names
del names[2]
print names

# 2: 分片赋值
names[3:] = list("haoxiaotian")
print names

a = [1,2,3]
b = [2,3,4]
# a.append(b)
a.extend(b)
print a


# 元组：不可变序列


