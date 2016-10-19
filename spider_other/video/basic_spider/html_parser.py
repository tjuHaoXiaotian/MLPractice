# coding=gb2312
import re
import urlparse

import bs4


class HtmlParser(object):

    def _get_new_urls_and_data(self, page_url, soup):
        # a /html/9/baxinniangganliaohuanshifenxuene16P/ 把新娘干了，还是粉穴呢[16P]
        new_urls = set()
        datas = []
        page_node = soup.find('div',class_="bm bw0 pgs cl")
        a_page_index = page_node.find_all('a', href=re.compile(r"forum-"))
        # print page_node

        form_node = soup.find('form', id="moderate")
        # print form_node
        a_node = form_node.find_all('a', class_="z")


        if a_node != None:
            for link in a_node:
                data = {}
                new_url,text =  link['href'], link['title']
                new_full_url = urlparse.urljoin(page_url,new_url)

                data["name"] = text
                data["url"] = new_full_url

                print data['name'], data['url']
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

