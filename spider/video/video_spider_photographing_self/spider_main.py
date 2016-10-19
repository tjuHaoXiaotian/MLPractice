# coding=utf-8
import os
import time

from spider.video.video_spider_photographing_self import datareader
from spider.video.video_spider_photographing_self import html_downloader
from spider.video.video_spider_photographing_self import html_parser

from spider.video.video_spider_photographing_self import html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = []
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.dataReader = datareader.DataReader()

    def craw(self, csv_url,base_dir):
        ISOTIMEFORMAT = "%Y-%m-%d %X"
        if not os.path.exists(base_dir):
            os.mkdir(base_dir)
        count = 1


        # fin
        self.urls = self.dataReader.read(csv_url)
        print "共",len(self.urls),"组视频："

        for item in self.urls:
            try:
                if count < 17:
                    count += 1
                    continue
                # else:
                #     print item["name"]
                #     continue
                # print item["name"]
                # print item["url"]
                # continue

                # print item["url"]
                response_data,dir_num = self.downloader.download(item["url"])
                # print response_data

                if dir_num == 0:
                    count += 1
                    continue


                new_video_url = self.parser.parse(response_data)
                # print new_img_urls
                print count, " : ", item["name"],":",new_video_url

                filePath = base_dir + "/" + str(count) + "_" + item["name"].strip().replace(" ","")
                # 创建视频文件夹
                if not os.path.exists(filePath):
                    os.mkdir(filePath)
                else:
                    os.mkdir(filePath+time.strftime(ISOTIMEFORMAT,time.localtime(time.time())))

                index = new_video_url.rfind('.')
                type = new_video_url[index:]
                print "video url",new_video_url

                file_name = filePath+"/"+"beauty"+type
                print file_name
                down_num = self.downloader.download_video(new_video_url,file_name)
                if down_num == 0:  # 如果整个文件夹下，video没有下载下来，则删除文件夹
                    print "delete ",filePath
                    os.rmdir(filePath)


                count += 1
            except Exception,e:
                print "craw failed\n",e
        # self.outputer.output_html(name)


if __name__ == "__main__":
    csv_url = "list.csv"
    base_dir = "d:/data"
    obj_spider = SpiderMain()
    obj_spider.craw(csv_url,base_dir)
