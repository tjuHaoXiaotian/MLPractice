# coding=gb2312
import re
import urlparse

import bs4


class HtmlParser(object):

    def _get_new_urls(self, soup):
        # <img src="http://111.qi50.com/1uploa13ds/article/uzvenvrw4yh.jpg">
        new_urls = set()
        div_nodes = soup.find('div',id="contain").find("center")
        img_nodes = div_nodes.findAll('img')
        # print len(img_nodes)
        for img in img_nodes:
            # print img['src']
            new_urls.add(img['src'])

        # print img_nodes
        return new_urls


    def parse(self, html_cont):
        if html_cont is None:
            return

        soup = bs4.BeautifulSoup(html_cont,'html.parser',from_encoding='gbk')
        new_urls = self._get_new_urls(soup)
        return new_urls

