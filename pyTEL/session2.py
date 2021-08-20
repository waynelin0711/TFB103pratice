import requests
from bs4 import BeautifulSoup
url='https://www.ptt.cc/bbs/Gossiping/index.html'
useragent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
headers={
'User-Agent':useragent
}
landingpageurl='https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html'
askover18url='https://www.ptt.cc/ask/over18'
pttgossipurl='https://www.ptt.cc/bbs/Gossiping/index.html'
#create session
ss=requests.session()
#get form data
reslandingpage= ss.get(landingpageurl, headers=headers)
souplandingpage=BeautifulSoup(reslandingpage.text, 'html.parser')
print(ss.cookies)

data= dict()
key1= souplandingpage.select('input')[0]['name']
value1= souplandingpage.select('input')[0]['value']
data[key1]= value1
key2= souplandingpage.select('button')[0]['name']
value2= souplandingpage.select('button')[0]['value']
data[key2]= value2
print(data)

ss.post(askover18url, headers=headers,data=data)
print(ss.cookies)

res=ss.get(pttgossipurl, headers=headers)
print(res.text)