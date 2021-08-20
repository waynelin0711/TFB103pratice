import requests
from bs4 import BeautifulSoup
url='https://www.ptt.cc/bbs/movie/index%s.html'
useragent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
headers={
'User-Agent':useragent
}
page=9511
for i in range(0,10):
    res= requests.get(url%(page), headers=headers)

    soup=BeautifulSoup(res.text, 'html.parser')

#titles = soup.select('a')
    titles =soup.select('div[class="title"]')

    for titleSoup in titles:
        title=titleSoup.select('a')[0].text
        articleurl='https://www.ptt.cc'+titleSoup.select('a')[0]['href']
        print(title)
        print('=======')
    page -=1