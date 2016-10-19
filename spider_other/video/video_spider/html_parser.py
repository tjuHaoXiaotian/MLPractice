# coding=gb2312
import re
import urlparse

import bs4


class HtmlParser(object):

    def _get_new_urls(self, soup):
        # <img src="http://111.qi50.com/1uploa13ds/article/uzvenvrw4yh.jpg">
        new_urls = set()
        table_node = soup.find('div',class_="pcb").find("table")
        # print table_node
        img_nodes = table_node.findAll('img')
        # print img_nodes
        # print len(img_nodes)
        for img in img_nodes:
            # print img['src']
            new_urls.add(img['file'])

        # print img_nodes
        # print new_urls
        return new_urls


    def parse(self, html_cont):
        if html_cont is None:
            return

        soup = bs4.BeautifulSoup(html_cont,'html.parser',from_encoding='gbk')
        new_urls = self._get_new_urls(soup)
        return new_urls

