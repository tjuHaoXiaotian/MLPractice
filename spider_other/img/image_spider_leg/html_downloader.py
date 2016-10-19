# coding=utf-8
import urllib
import urllib2

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        try:
            request = urllib2.Request(url)
            request.add_header("user-agent", "Mozilla/5.0")

            # request.
            # response = urllib2.urlopen(url)
            response = urllib2.urlopen(request, data=None, timeout=10)

            if response.getcode() != 200:
                return None

            print url
            return response.read(),1
        except:
            print "can't get this dir or image :",url
            return None,0

    def Schedule(self,a, b, c):
        '''''
        a:已经下载的数据块
        b:数据块的大小
        c:远程文件的大小
       '''
        per = 100.0 * a * b / c
        if per > 100:
            per = 100
        print '%.2f%%' % per

    def download_file(self, url,file_name):
        print file_name
        if url is None:
            return 0
        try:
            urllib.urlretrieve(url, file_name)
            return 1
        except:
            print "can't get this dir or image :", url
            return 0
        # finally:
            # print "download this:",file_name

