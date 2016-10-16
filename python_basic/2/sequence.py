# coding=utf-8

# 六种内建序列： list、元组、字符串、u 字符串、

greeting = "hello"
print greeting[0]

print greeting[-1]

# 根据给定的年月日，以数字形式打印出日期
months = [
    'january',
    'february',
    'march',
    'april',
    'may',
    'june',
    'july',
    'august',
    'september',
    'october',
    'november',
    'december'
]

# 以1~31的数字作为结尾的列表
endings = ['st','nd','rd'] + 17 * ['th'] \
    + ['st','nd','rd'] + 7 * ['th'] \
    +['st']
year = raw_input("Year:")
# help(raw_input)
month = raw_input("Month (1-12): ")
day = raw_input("Day (1-31): ")

month_number = int(month)
day_number = int(day)

month_name = months[month_number-1]
ordinal = day + endings[day_number-1]

print month_name + ' ' + ordinal + ',' + year

