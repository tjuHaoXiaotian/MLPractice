# coding=gb2312
import re
import urlparse

import bs4


class HtmlParser(object):

    def _get_new_urls(self, soup):
        # <img src="http://111.qi50.com/1uploa13ds/article/uzvenvrw4yh.jpg">
        video_node = soup.find('div',id="contain").find("video")
        source_node = video_node.find('source')
        new_url = source_node['src']
        return new_url


    def parse(self, html_cont):
        if html_cont is None:
            return

        soup = bs4.BeautifulSoup(html_cont,'html.parser',from_encoding='gbk')
        new_urls = self._get_new_urls(soup)
        return new_urls

