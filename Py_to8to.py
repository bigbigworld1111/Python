# -*- coding:utf-8 -*-
import urllib2,cookielib,re,urllib,random,linecache

c = cookielib.LWPCookieJar() # 创建一个可以保存cooke的对象
cookie = urllib2.HTTPCookieProcessor(c)
opener = urllib2.build_opener(cookie)


count = len(open('xxx.txt','rU').readlines())

def login(user,pwd):
    url  = 'http://www.to8to.com/new_login.php'
    data = 'ismd5=0&referer=http%3A%2F%2Fwww.to8to.com%2F&val='+user+'&password=' +pwd
    req = urllib2.Request(url,data= data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36')
    html =opener.open(req).read()
    #print html
    if user in html:
        return True
    else:
        return False

def post(sid,uid,did,content):
    url = 'http://www.to8to.com/riji/ajaxpost.php'
    data={
        "act":"add_comments",
        "sid":sid,
        "uid":uid,
        "did":did,
        "content":content,
        "tgt_type":2,
        "ref_comment_id":"",
        "ref_comment_user_id":"",
        "parent_comment_id":""
    }

    data = urllib.urlencode(data)
    html = opener.open(url,data=data).read()

def getid(url):
    html = opener.open(url).read()
    reg=r"var gdid = '(.*?)'"
    sid =re.findall(reg,html)[0]

    reg = r'var owner_id = "(.*?)"'
    uid=re.findall(reg,html)[0]

    reg=r'id="diary-(.*?)"'
    did = re.findall(reg,html)[0]

    ran = random.randrange(1,count)
    content = linecache.getline('xxx.txt',ran)
    print content
    print sid,uid,did
    #post(sid,uid,did,content)

def getlist():
    html = opener.open('http://www.to8to.com/riji/hz').read()
    #print html
    reg = r'class="diary_author" href="(.*?)"'
    for i in re.findall(reg,html):
        getid(i)

if login('ddasjiie','1qaz2wsx'):
    print 'Login Success'
    ran = random.randrange(1,count)
    content = linecache.getline('xxx.txt',2)
    print count
    print ran
    print content
    #getlist()
else:
    print 'Login Fail'
