# -*- coding:utf-8 -*-

import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    page.close()
    return html
def getImg(html):
    #reg = 'src="(.*?.jpg)" width'
    reg = 'src="(.*?.jpg)" bdwater='
    imgre = re.compile(reg)
    imgList = imgre.findall(html)
    i = 0
    for imgurl in imgList:
        print "共%d张图片,正在下载第%d张得图片"%(len(imgList),i+1)
        urllib.urlretrieve(imgurl,"photo/%d.jpg"%(i,))
        i+=1

#ht = getHtml(r"http://tieba.baidu.com/p/2256306796")
ht = getHtml(r"http://tieba.baidu.com/p/2198660859?fr=good")
#print ht
print "#######################"
print getImg(ht)
