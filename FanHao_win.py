#-*- coding: cp936 -*
#cp936
#from pip.backwardcompat import raw_input
import urllib2
import re
import random
import webbrowser
import sys

print '#'*50
print '#'+'����������'
print '#'*50
print '-'*20+'��ʼ��ȡ����'+'-'*20

proxy_txt = open('proxy_list.txt','w')
proxy_tr = re.compile("(?isu)<tr[^>]*>(.*?)</tr>")
proxy_td = re.compile("(?isu)<td[^>]*>(.*?)</td>")
proxy_ua = {'User-Agent:':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}
proxy_url = urllib2.Request(url='http://www.site-digger.com/html/articles/20110516/proxieslist.html',headers=proxy_ua)
try:
    GetProxy = urllib2.urlopen(proxy_url)
    HtmlRead = GetProxy.read()
except Exception:
    print '-'*50
    print '�ɼ���������������������Ƿ�������'
    print '-'*50
    raw_input('���س���������:')
else:
    for row in proxy_tr.findall(HtmlRead):
        for col in proxy_td.findall(row)[:1]:
            proxy_txt.write(col+'\n')
    proxy_txt.close()

print '-'*20+'��ȡ�������'+'-'*20

open_proxy = open('proxy_list.txt','r')
line0 = open_proxy.readlines()
open_proxy.close()

proxy_line = random.choice(line0)
proxy_handler = urllib2.ProxyHandler({'http://':'%s'%proxy_line})
opener = urllib2.build_opener(proxy_handler)
urllib2.install_opener(opener)

print '#'*50
print '##���鹫������'
print '##��Ŀ��ҳ: FanHao.miaowu.asia'
print '#'*50
Fanhao = raw_input('�����뷬��:')

FanHao_style = open('FanHao.html','w')
FanHao_NR = '<link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.2.0/css/bootstrap.min.css">'+'\n'+'<center><h3>���鹫�ӷ��Ųɼ���</h3><hr/><p>�����������Դ�����磬������������ϵ����</p><br/><table class="table table-striped table-hover"></center>'
FanHao_style.write(FanHao_NR)
FanHao_style.close()

Fanhao_html = open('FanHao.html','a')
ZhuaQ_LJ = re.compile('(?isu)<table class="torrent_name_tbl">(.*?)</table>')
proxy_ua = {'User-Agent:':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36','Accept-Language:':'zh-CN,zh;q=0.8'}
proxy_url = urllib2.Request(url='https://btdigg.org/search?info_hash=&q='+Fanhao ,headers=proxy_ua)

GetProxy = urllib2.urlopen(proxy_url)
HtmlRead = GetProxy.read()
for LianJ in ZhuaQ_LJ.findall(HtmlRead):
        type2 = sys.getfilesystemencoding()
        xieru = LianJ.decode('utf-8').encode(type2)
        Fanhao_html.write(xieru+'\n')
        

Fanhao_html.close()
#
FanHao_style_end = open('FanHao.html','a')
FanHao_NR_end = '</table>'
FanHao_style_end.write(FanHao_NR_end)
FanHao_style_end.close()
def tihuan(tiH,tiH2):
    TiHuan='FanHao.html'
    fp=open(TiHuan,'r')
    alllines=fp.readlines()
    fp.close()
    fp=open(TiHuan,'w')
    for eachline in alllines:
        a=re.sub(tiH,tiH2,eachline)
        fp.writelines(a)
    fp.close()

dl2 = tihuan('title="Add to BTCloud"','style="display:none;"')
dl3 = tihuan('class="attr_name"','style="display:none;"')
dl4 = tihuan('class="attr_val"','style="display:none;"')
dl5 = tihuan('magnet-link','��������')

dl2
dl3
dl4
dl5

print '#'*50
print '>'*10+'���Ż�ȡ�ɹ�'
print '#'*50

raw_input('���س��鿴���:')

open_url = webbrowser.open("FanHao.html")

open_url