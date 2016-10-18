#coding=utf-8
import os

url = "http://sss.ws6f.com:7799/video/category/uploa14ds/article/34lgsett1wn.mp4"
import urllib


def Schedule( a, b, c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print '%.2f%%' % per

file_name = "d:/data/1_普通话 天津 河东区 阿静/2016-10-18 17:59:17.mp4".replace(" ","")
print file_name
urllib.urlretrieve(url,"d:/data/普通话天津河东区阿静/test.mp4".decode("utf-8"), Schedule)