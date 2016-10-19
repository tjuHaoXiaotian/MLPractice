# coding=utf-8

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self,data):
        if data is None:
            return
        self.datas.extend(data)

    pass

    def output_html(self,name):
        fout = open(name + '.html', 'w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        for item in self.datas:
            # print "item",item
            fout.write("<tr>")
            # print item['name']
            fout.write("<td> %s </td>" % item['name'].encode("utf-8"))
            fout.write("<td> %s </td>" % item["url"])
            fout.write("</tr>")
            # fout.write("<div> %s </div>" % img["name"].encode('utf-8'))
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()

    def output_csv(self, name):
        fout = open(name + '.csv', 'w')

        for item in self.datas:
            # print "item",item
            # print item['name']
            fout.write(item['name'].encode("utf-8"))
            fout.write(",")
            fout.write(item['url'].encode("utf-8"))
            fout.write("\n")
            # fout.write("<div> %s </div>" % img["name"].encode('utf-8'))
        fout.close()