# coding=utf-8 ##
__author__ = 'seany'



#到豆瓣电影列表抓去大于等于8分的电影#
#http://movie.douban.com/tag/%E5%8A%A8%E4%BD%9C?start=0&type=T
import urllib2
import re
import sys

# 获取当前系统编码格式
type = sys.getfilesystemencoding()
j = 0
for i in range(0, 1000, 20):
    #url = 'http://movie.douban.com/tag/%E5%8A%A8%E4%BD%9C?'
    url = 'http://movie.douban.com/tag/动作?'
    hash = 'start=%d&type=S' % i
    url = url + hash
    print(url)
    # 读取url内容
    content = urllib2.urlopen(url).read()
    # 转换编码
    content = content.decode("UTF-8").encode(type)
    # 读取电影名称
    match = re.findall(r' <a class="nbg".*?title=(.*?)>', content)
    # 读取分数
    match2 = re.findall(r'<span class="rating_nums">(.*?)</span>', content)
    #print len(match2)
    # 读取评论数
    match_3 = re.findall(r'<span class="pl">\((\d+)'.encode("gbk"), content)
    # print "match_3 is:", len(match_3)
    for i in range(0,len(match2)):
        #大于8分的电影
        if match2[i]!="":
            if float(match2[i])>=8:
                 j = j + 1
                 print match[i]+"   "+match2[i]
print ('总共抓取电影数据'+ str(j) +'条').decode("UTF-8").encode(type)
print 'done'