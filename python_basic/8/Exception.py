# coding=utf-8

# 异常处理

# raise Exception


try:
    num =  1 / 0
except ZeroDivisionError,e:
    print e
else:
    print "work well!"
finally:
    print "clean up ..."

