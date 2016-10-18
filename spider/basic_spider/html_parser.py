# coding=gb2312
import re
import urlparse

import bs4


class HtmlParser(object):

    def _get_new_urls_and_data(self, page_url, soup):
        # a /html/9/baxinniangganliaohuanshifenxuene16P/ 把新娘干了，还是粉穴呢[16P]
        new_urls = set()
        datas = []
        div_node = soup.find('div', id="contain")

        a_node = div_node.find_all('a', href=re.compile(r"/html"))
        if a_node != None:
            for link in a_node:
                data = {}
                new_url,text =  link['href'], link.get_text()
                new_full_url = urlparse.urljoin(page_url,new_url)
                # print text,new_full_url
                # 熟?PK?女－狗狗?屁股???[18P] http://www.hf1z.com/html/9/shufuPKtanvgougouguopiguaoyunhui18P/
                # ?妻系列之?羞?臊的性奴生活[12P] http://www.hf1z.com/html/9/saoqixiliezhimeixiumeisaodexingnushenghuo12P/
                # 床上?各?高??作[12P] http://www.hf1z.com/html/9/chuangshangjingeergaonandongzuo12P/


                # 2 http://www.hf1z.com/html/9/index2.html
                # 3 http://www.hf1z.com/html/9/index3.html
                # 4 http://www.hf1z.com/html/9/index4.html
                # 5 http://www.hf1z.com/html/9/index5.html
                # 6 http://www.hf1z.com/html/9/index6.html
                # 7 http://www.hf1z.com/html/9/index7.html
                # 8 http://www.hf1z.com/html/9/index8.html
                # 9 http://www.hf1z.com/html/9/index9.html
                # 10 http://www.hf1z.com/html/9/index10.html
                # 下一页 http://www.hf1z.com/html/9/index2.html
                # 尾页 http://www.hf1z.com/html/9/index37.html

                if new_full_url.endswith('.html'):
                    new_urls.add(new_full_url)
                else:
                    data["name"] = text
                    data["url"] = new_full_url
                    datas.append(data)
        return new_urls,datas



    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = bs4.BeautifulSoup(html_cont,'html.parser',from_encoding='gbk')
        new_urls,new_data = self._get_new_urls_and_data(page_url,soup)
        return new_urls,new_data

