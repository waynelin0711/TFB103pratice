from urllib import request
import ssl
url = 'https://www.ptt.cc/bbs/joke/index.html'
useragent= 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
headers={
'User-Agent':useragent
}
req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
# res = request.urlopen(url=url)
html=res.read().decode('utf-8')
print(html)
