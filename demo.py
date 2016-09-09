import urllib.request
import urllib.error
import re
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
try:
    pass
    requset = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(requset)
    content = response.read().decode('utf-8')
    pattern = re.compile(
        '<div.*?author.*?<h2>(.*?)</h2>.*?<span>(.*?)</span', re.S)
    items = re.findall(pattern, content)
    for item in items:
        print('author: ' + item[0])
        print('content: ' + item[1])
        print()
except urllib.error.URLError as e:
    if hasattr(e, 'code'):
        print(e.codes)
    if hasattr(e, 'reson'):
        print(e.reson)
