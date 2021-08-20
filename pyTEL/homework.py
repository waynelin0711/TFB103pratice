import requests
from bs4 import BeautifulSoup

url='http://ec2-13-114-140-26.ap-northeast-1.compute.amazonaws.com/practice/tfb103'
useragent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
headers={
'User-Agent':useragent
}
cookies={
class_id=tfb103; Path=/
}
ss.cookies['over18']='1'
res =ss.get(url, headers=headers)
print(res.text)