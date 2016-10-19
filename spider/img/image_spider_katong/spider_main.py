# coding=utf-8
import os
import time

from spider.img.image_spider_katong import datareader
from spider.img.image_spider_katong import html_downloader
from spider.img.image_spider_katong import html_outputer
from spider.img.image_spider_katong import html_parser


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
        print "共",len(self.urls),"组图片："

        for item in self.urls:
            try:
                # if count < 1:
                #     count += 1
                #     continue
                # else:
                #     print item["name"]
                #     continue

                # print item["url"]
                response_data,dir_num = self.downloader.download(item["url"])
                # print response_data

                if dir_num == 0:
                    count += 1
                    continue


                new_img_urls = self.parser.parse(response_data)
                # print new_img_urls
                print count, " : ", item["name"],";共:", len(new_img_urls), "张"

                # 创建图片文件夹
                if not os.path.exists(base_dir+"/"+item["name"].strip()):
                    os.mkdir(base_dir+"/"+str(count)+"_"+item["name"].strip())
                else:
                    os.mkdir(base_dir+"/"+str(count)+"_"+item["name"].strip()+time.strftime( ISOTIMEFORMAT,time.localtime(time.time())))

                img_index = 0
                num = 0
                for img_url in new_img_urls:
                    index = img_url.rfind('.')
                    type = img_url[index:]
                    img_data,down_num = self.downloader.download(img_url)
                    num+=down_num

                    if img_data == None or down_num == 0:
                        print "img continue"
                        continue

                    self.dataReader.write(base_dir+"/"+str(count)+"_"+item["name"].strip(),img_data,img_index,type)
                    img_index += 1
                    # print type
                if num == 0:  # 如果整个文件夹下，一张图片都没有下载下来，则删除文件夹
                    print "delete ",base_dir+"/"+str(count)+"_"+item["name"].strip()
                    os.rmdir(base_dir+"/"+str(count)+"_"+item["name"].strip())
                count += 1
            except Exception,e:
                print "craw failed\n",e
        # self.outputer.output_html(name)


if __name__ == "__main__":
    csv_url = "list.csv"
    base_dir = "/home/haoxiaotian/girl/cartoon"
    obj_spider = SpiderMain()
    obj_spider.craw(csv_url,base_dir)
