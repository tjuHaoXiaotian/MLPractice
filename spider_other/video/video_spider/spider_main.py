# coding=utf-8
import os
import time

from spider_other.video.video_spider import datareader
from spider_other.video.video_spider import html_downloader
from spider_other.video.video_spider import html_outputer

from spider_other.img.image_spider import html_parser


class SpiderMain(object):
    def __init__(self):
        self.urls = []
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.dataReader = datareader.DataReader()


    def craw(self, csv_url, base_dir,log_file):
        ISOTIMEFORMAT = "%Y-%m-%d %X"
        if not os.path.exists(base_dir):
            os.mkdir(base_dir)
        count = 1

        # fin
        self.urls = self.dataReader.read(csv_url)
        print "共", len(self.urls), "组图片："

        total_download = 0
        total_download_pre = 0
        total_failed = 0
        for item in self.urls:
            try:
                if count < 3:
                    count += 1
                    continue
                # else:
                #     print item["name"]
                #     continue

                # print item["url"]
                response_data, dir_num = self.downloader.download(item["url"])
                # print response_data

                if dir_num == 0:
                    count += 1
                    continue

                new_img_urls = self.parser.parse(response_data)
                # print new_img_urls
                print count, " : ", item["name"], ";共:", len(new_img_urls), "个文件"

                dir_path = base_dir + "/" + str(count) + "_" + item["name"].strip()
                # 创建图片文件夹
                if not os.path.exists(base_dir + "/" + item["name"].strip()):
                    os.mkdir(dir_path)
                else:
                    os.mkdir(dir_path + time.strftime(ISOTIMEFORMAT, time.localtime(time.time())))

                img_index = 0
                num = 0

                total_download += len(new_img_urls)  # 总下载数
                for img_url in new_img_urls:
                    index = img_url.rfind('.')
                    type = img_url[index:]
                    file_name = dir_path + "/" + str(img_index) + type
                    if type == '.jpg':
                        down_num = self.downloader.download_img(img_url,self.dataReader,file_name)
                    elif type == '.mp4':
                        down_num = self.downloader.download_file(img_url,file_name)
                    num += down_num

                    # 下载失败，重新尝试
                    fail_time = 1
                    while down_num == 0 and fail_time <= 3:  # 下载失败并且尝试次数 < 3 次，继续尝试
                        print "downlaod failed,retry time:", fail_time
                        if type == '.jpg':
                            down_num = self.downloader.download_img(img_url, self.dataReader, file_name)
                        elif type == '.mp4':
                            down_num = self.downloader.download_file(img_url, file_name)
                        fail_time += 1

                    # 3 次尝试后，仍然失败，跳出循环，继续下一个 url
                    if down_num == 0:
                        total_failed += 1  # 总失败数
                        continue


                    img_index += 1
                    # print type
                if num == 0:  # 如果整个文件夹下，一张图片都没有下载下来，则删除文件夹
                    os.rmdir(dir_path)
                    print "delete ", dir_path

                    # record to the log
                    log = {}
                    log["time"] = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
                    log["log"] = "download failed: remove "+ dir_path
                    self.outputer.output_log(log_file, log)

                count += 1

                if total_download - total_download_pre > 2:
                    print "total download: ", total_download, " failed: ", total_failed, " failed rate: ", total_failed / float(total_download)
                    total_download_pre = total_download

                    # record to the log
                    log = {}
                    log["time"] = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
                    log["log"] = "total download: " + str(total_download) + " failed: " + str(\
                        total_failed) + " failed rate: " + str(total_failed / float(total_download))
                    self.outputer.output_log(log_file,log)

                    break
            except Exception, e:
                print "craw failed\n", e
                # self.outputer.output_html(name)


if __name__ == "__main__":
    csv_url = "resources/偷拍自拍-偷偷撸影院.csv"
    base_dir = "/home/haoxiaotian/偷偷撸2014在线影院/video/偷拍自拍"
    log_file = "logs/log.偷拍自拍"
    # base_dir = "d:/data_image"
    obj_spider = SpiderMain()
    obj_spider.craw(csv_url,base_dir,log_file)