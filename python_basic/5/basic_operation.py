# coding=utf-8

# 序列解包
x,y,z = 1,2,3
print x,y,z

x,y = y,x
print x,y,z

# 列表推导式
result = [x*x for x in range(0,10)]
print result

result = [x for x in result if x % 2 == 0]
print result

# pass:空白执行；
# del：只会删除名称




