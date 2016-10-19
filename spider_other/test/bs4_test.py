# coding=utf-8
import re

from bs4 import BeautifulSoup

html_doc ="""
<div id="contain">
<div class="lblmain">
<div class="index_box">
<h2>偷拍自拍</h2>
<div class="zxlist">
<script type="text/javascript" language="javascript" src="http://sss.sege.xxx/guanggao.js"></script><li><a href="http://www.x158.tv/xpjs34.html" target="_blank">【澳门新葡京赌场】投注1元起，天天返水3.0%无上限，提款3分钟火速到账！</a> <span>广告</span></li>
<li><a href="http://www.yin6666.net/yhs26.html" target="_blank">【澳门银河娱乐城12.net】BBIN顶级信誉，天天返水2.0%无上限，=澳门银河官方直营=【注册免费自动送12元】 </a> <span>广告</span></li>
<li><a href="http://www.jinshavip678.com/jss13.html" target="_blank">【澳门金沙官方赌场】亚洲第一顶级线上娱乐！业界信誉最高，存取款秒到!天天返水高达2.0%无上限！</a> <span>广告</span></li>
<li><a href="http://www.yl680.com/yls12.html" target="_blank"><font color="#FF0000">【永利娱乐城】注册即送12元免费试玩金,最高可获奖金777元,品牌信誉,大额无忧 </font></a> <span>广告</span></li>


<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="把新娘干了，还是粉穴呢[16P]" border="0"> <a href="/html/9/baxinniangganliaohuanshifenxuene16P/" target="_blank">把新娘干了，还是粉穴呢[16P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-10-02</font> </li>
</ul>

<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="騷貨真不错一般，射了她滿嘴[10P]" border="0"> <a href="/html/9/saohuozhenbucuoyibansheliaotamanzui10P/" target="_blank">騷貨真不错一般，射了她滿嘴[10P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-10-02</font> </li>
</ul>

<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="情趣內衣、網襪、C字褲的誘惑[14P]" border="0"> <a href="/html/9/qingqunayijinyaoCzixuandezhahuo14P/" target="_blank">情趣內衣、網襪、C字褲的誘惑[14P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-09-27</font> </li>
</ul>

<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="女嘉宾私密照外泄[10P]" border="0"> <a href="/html/9/nvjiabinsimizhaowaixie10P/" target="_blank">女嘉宾私密照外泄[10P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-09-27</font> </li>
</ul>

<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="人妻在宾馆自拍[12P]" border="0"> <a href="/html/9/renqizaibinguanzipai12P/" target="_blank">人妻在宾馆自拍[12P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-09-27</font> </li>
</ul>

<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="我的小女友，化不化妆真的不一样1[30P]" border="0"> <a href="/html/9/wodexiaonvyouhuabuhuazhuangzhendebuyiyang130P/" target="_blank">我的小女友，化不化妆真的不一样1[30P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-09-27</font> </li>
</ul>

<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="森北路傳播妹嘉楠和男友酒店愛愛[33P]" border="0"> <a href="/html/9/senbeiluchuanbomeijiananhenanyoujiudianaiai33P/" target="_blank">森北路傳播妹嘉楠和男友酒店愛愛[33P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-09-27</font> </li>
</ul>

<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="又一个92年清纯嫩女骚样自拍照流出[18P]" border="0"> <a href="/html/9/youyige92nianqingchunnennvsaoyangzipaizhaoliuchu18P/" target="_blank">又一个92年清纯嫩女骚样自拍照流出[18P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-09-26</font> </li>
</ul>

<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="人妻在宾馆自拍[12P]" border="0"> <a href="/html/9/renqizaibinguanzipai12P/" target="_blank">人妻在宾馆自拍[12P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-09-26</font> </li>
</ul>

<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="騷貨真不错一般，射了她滿嘴[10P]" border="0"> <a href="/html/9/saohuozhenbucuoyibansheliaotamanzui10P/" target="_blank">騷貨真不错一般，射了她滿嘴[10P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-09-26</font> </li>
</ul>

<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="最近約上的少婦，床上功夫非一般的牛[22P]" border="0"> <a href="/html/9/zuijinjishangdeshaofuchuangshanggongfufeiyibandeniu22P/" target="_blank">最近約上的少婦，床上功夫非一般的牛[22P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-09-26</font> </li>
</ul>

<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="捆綁三個小母狗[11P]" border="0"> <a href="/html/9/kunjiansangexiaomugou11P/" target="_blank">捆綁三個小母狗[11P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-09-26</font> </li>
</ul>

<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="前幾天約了一個，特來分享[15P]" border="0"> <a href="/html/9/qianjitianjiliaoyigetelaifenxiang15P/" target="_blank">前幾天約了一個，特來分享[15P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-09-26</font> </li>
</ul>

<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="朋友老婆自拍照[14P]" border="0"> <a href="/html/9/pengyoulaopozipaizhao14P/" target="_blank">朋友老婆自拍照[14P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-09-25</font> </li>
</ul>

<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="騷貨真不错一般，射了她滿嘴[10P]" border="0"> <a href="/html/9/saohuozhenbucuoyibansheliaotamanzui10P/" target="_blank">騷貨真不错一般，射了她滿嘴[10P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-09-25</font> </li>
</ul>

<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="女嘉宾私密照外泄[10P]" border="0"> <a href="/html/9/nvjiabinsimizhaowaixie10P/" target="_blank">女嘉宾私密照外泄[10P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-09-25</font> </li>
</ul>

<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="浓毛老婆快捷酒店搔首弄姿的诱惑[12P]" border="0"> <a href="/html/9/nongmaolaopokuaijiejiudiansaoshounongzideyouhuo12P/" target="_blank">浓毛老婆快捷酒店搔首弄姿的诱惑[12P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-09-25</font> </li>
</ul>

<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="女友闺蜜的私照[20P]" border="0"> <a href="/html/9/nvyouguimidesizhao20P/" target="_blank">女友闺蜜的私照[20P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-09-25</font> </li>
</ul>

<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="熟婦PK處女－狗狗國屁股奧運會[18P]" border="0"> <a href="/html/9/shufuPKtanvgougouguopiguaoyunhui18P/" target="_blank">熟婦PK處女－狗狗國屁股奧運會[18P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-09-24</font> </li>
</ul>

<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="佛門之地, 不帶一絲煩惱[14P]" border="0"> <a href="/html/9/fomenzhidibudaiyijianfannao14P/" target="_blank">佛門之地, 不帶一絲煩惱[14P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-09-23</font> </li>
</ul>

<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="熟妇长的难看，但她的肥麻批还比较嫩！凑合着看下[10P]" border="0"> <a href="/html/9/shufuchangdenankandantadefeimapihuanbijiaonencouhezhuokanxia10P/" target="_blank">熟妇长的难看，但她的肥麻批还比较嫩！凑合着看下[10P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-09-23</font> </li>
</ul>

<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="佛門之地, 不帶一絲煩惱[14P]" border="0"> <a href="/html/9/fomenzhidibudaiyijianfannao14P/" target="_blank">佛門之地, 不帶一絲煩惱[14P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-09-22</font> </li>
</ul>

<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="熟婦PK處女－狗狗國屁股奧運會[18P]" border="0"> <a href="/html/9/shufuPKtanvgougouguopiguaoyunhui18P/" target="_blank">熟婦PK處女－狗狗國屁股奧運會[18P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-09-22</font> </li>
</ul>

<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="騷妻系列之沒羞沒臊的性奴生活[12P]" border="0"> <a href="/html/9/saoqixiliezhimeixiumeisaodexingnushenghuo12P/" target="_blank">騷妻系列之沒羞沒臊的性奴生活[12P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-09-20</font> </li>
</ul>

<ul>

<li> <img src="/template/sdl/images/a74e55b4jw1e18mycmbyvg.gif" alt="床上練各種高難動作[12P]" border="0"> <a href="/html/9/chuangshangjingeergaonandongzuo12P/" target="_blank">床上練各種高難動作[12P]</a></li>
<li class="zxsyd"> <font color="#3C3C3C">2016-09-20</font> </li>
</ul>

</div>
    <div class="box_page">
        <div class="pages"><span>共904条数据 页次:1/37页</span><em class="nolink">首页</em><em class="nolink">上一页</em><span><font color="red">1</font></span><a href="/html/9/index2.html">2</a><a href="/html/9/index3.html">3</a><a href="/html/9/index4.html">4</a><a href="/html/9/index5.html">5</a><a href="/html/9/index6.html">6</a><a href="/html/9/index7.html">7</a><a href="/html/9/index8.html">8</a><a href="/html/9/index9.html">9</a><a href="/html/9/index10.html">10</a><a href="/html/9/index2.html">下一页</a><a href="/html/9/index37.html">尾页</a><span><input name="page" size="4" type="input"><input value="跳转" onclick="getPageGoUrl(37,'page','/html/9/index<page>.html')" class="btn" type="button"></span></div>
        <div class="clear"></div>
      </div>
          </div>
     </div>
 </div>

"""

soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')

# print '获取所有的链接'
# links = soup.find_all('a')
# for link in links:
#     print link.name,link['href'],link.get_text()

# print "正则表达式"
# link_node = soup.find('a',href=re.compile(r"http://jianyi.baidu.com/"))
#
# print link_node.name, link_node['href'], link_node.get_text()



print "获取div段落文字"
div_node = soup.find('div',id="contain")

a_node = div_node.find_all('a',href=re.compile(r"/html"))
for link in a_node:
    print link.name,link['href'],link.get_text()









