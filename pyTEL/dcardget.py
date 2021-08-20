from urllib import request
import ssl
import os
import requests
import json

if not os.path.exists ('./dcardphoto/'):
    os.mkdir('./dcardphoto/')
url='https://www.dcard.tw/service/api/v2/forums/photography/featuredPosts'
useragent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
headers={
'User-Agent':useragent
}
res =requests.get(url, headers=headers)
#print(res.text)
jsondata= json.loads(res.text)
for r in jsondata:
    print(r)
print(jsondata[0].keys())
for k in jsondata[0]:
    print(k)
print(jsondata[1]['mediaMeta'])
for i in jsondata[1]['mediaMeta']:
    print(i)
    print(i['url'])

for articledict in jsondata:
    title=articledict['title']
    articleurl='https://www.dcard.tw/f/photography/p/' +str(articledict['id'])
    print(title)
    print(articleurl)
    for imgs in articledict['mediaMeta']:
        print('\t'+imgs['url'])
        #imagepath='./dcardphoto/{}.{}'.format(title, imgs['url'].split('.')[-1])
        imagepath = './dcardphoto/{}_{}'.format(title,imgs['url'].split('/')[-1])
        #request.urlretrieve(imgs['url'], './dcardphoto/')
        imgcontent=requests.get(imgs['url'], headers=headers).content
        with open('dcardphoto' , 'wb') as f:
            f.write(imgcontent)
    print('=======')



