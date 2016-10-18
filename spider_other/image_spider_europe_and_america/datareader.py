# coding=utf-8

import csv
import sys
reload(sys)
sys.setdefaultencoding('utf8')
class DataReader:
    def read(self, filepath):
        globalArray = []
        file_object = open(filepath)

        try:
            for line in file_object:
                array = line.split(',')
                dic = {}
                dic["name"] = array[0].decode("utf-8")
                # print dic['name']
                dic["url"] = array[1]
                globalArray.append(dic)
        finally:
            file_object.close()


        # csvfile = file(filepath, 'rb')
        # reader = csv.reader(csvfile)

        # i = 0
        # for name,url in reader:
        #     item = {}
        #     item["name"] = name
        #     item["url"] = url
        #     globalArray.append(item)
        # csvfile.close()
        return globalArray


    def write(self,filepath,data,name,type):
        # print filepath+"/"+str(name) + type
        # print data
        fout = open(filepath+"/"+str(name) + type, 'w')
        fout.write(data)
        fout.close()
