# coding=gb2312
import re
import urlparse

import bs4


class HtmlParser(object):

    def _get_new_urls_and_data(self, page_url, soup):
        new_urls = set()
        datas = []
        page_node = soup.find('div',class_="bm bw0 pgs cl")
        a_page_index = page_node.find_all('a', href=re.compile(r"forum-48"))
        # print page_node

        table_node = soup.find('table', id="threadlisttableid")
        a_node = table_node.find_all('a', class_="s xst")


        if a_node != None:
            for link in a_node:
                data = {}
                new_url,text =  link['href'], link.get_text()
                new_full_url = urlparse.urljoin(page_url,new_url)

                data["name"] = text
                data["url"] = new_full_url
                datas.append(data)
            for link in a_page_index:
                new_url = link['href']
                new_full_url = urlparse.urljoin(page_url, new_url)
                new_urls.add(new_full_url)
            # print new_urls
            # print datas
        return new_urls,datas



    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = bs4.BeautifulSoup(html_cont,'html.parser',from_encoding='gbk')
        new_urls,new_data = self._get_new_urls_and_data(page_url,soup)
        return new_urls,new_data

