
from urllib import request
import ssl
url=' https://c6270aae083f.ngrok.io/hello_get?name=Allen'
res = request.urlopen(url=url)
html=res.read().decode('utf-8')
print(html)






















