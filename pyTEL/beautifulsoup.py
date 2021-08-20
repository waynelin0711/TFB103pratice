from urllib import request
from bs4 import BeautifulSoup
import ssl
url = 'https://www.ptt.cc/bbs/joke/index.html'
useragent= 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
headers={
'User-Agent':useragent
}
req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
#res = request.urlopen(url=url)
#get html script
html=res.read().decode('utf-8')
#print(html)

soup=BeautifulSoup(html,'html.parser')
#print(soup)

#return a list
logo=soup.findAll('a',{'id':'logo'})
logo=soup.findAll('a',id='logo')
print(logo[0])
print(logo[0].text)
print('https://www.ptt.cc'+logo[0]['href'])
