# coding=utf-8
from spider_other.video.basic_spider import html_downloader
from spider_other.video.basic_spider import html_outputer
from spider_other.video.basic_spider import url_manager

from spider_other.img.basic_spider import html_parser


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url,name):
        count = 1

        self.urls.add_new_url(root_url)

        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print "craw %d : %s " %(count,new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)

                # print new_urls
                # print new_data
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count % 10 == 0:
                    self.outputer.output_csv(name)
                    self.outputer.datas = []

                count += 1
            except:
                print "craw failed"
        self.outputer.output_csv(name)


if __name__ == "__main__":
    # root_url = "http://www.pppav7171.net/forum-58-1.html" #偷拍自拍
    # name = '偷拍自拍-偷偷撸影院'

    root_url = "http://www.pppav7171.net/forum-62-1.html" #欧美性爱
    name = '欧美性爱-偷偷撸影院'

    obj_spider = SpiderMain()
    obj_spider.craw(root_url,name)
