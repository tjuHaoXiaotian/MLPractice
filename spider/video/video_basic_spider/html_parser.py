# coding=gb2312
import re
import urlparse

import bs4


class HtmlParser(object):

    def _get_new_urls_and_data(self, page_url, soup):
        new_urls = set()
        new_video_urls = set()
        datas = []

        a_node = soup.find_all('a', href=re.compile(r"/html"))
        # print len(a_node)
        if a_node != None:
            for link in a_node:
                data = {}
                new_url, text = link['href'], link.get_text()
                new_full_url = urlparse.urljoin(page_url, new_url)

                if new_full_url.endswith('.html'):
                    new_urls.add(new_full_url)
                else:
                    if text != None and (new_url not in new_video_urls):
                        new_video_urls.add(new_url)
                        data["name"] = text
                        data["url"] = new_full_url
                        datas.append(data)
                        # print data
            print len(new_urls)
        return new_urls, datas



    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = bs4.BeautifulSoup(html_cont,'html.parser',from_encoding='gbk')
        new_urls,new_data = self._get_new_urls_and_data(page_url,soup)
        return new_urls,new_data

