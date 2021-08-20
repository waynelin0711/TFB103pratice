

import re, time, requests

from bs4 import BeautifulSoup
import csv
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
url = "https://www.104.com.tw/jobs/search/?ro=1&kwop=1&expansionType=job&area=6001001000&order=15&asc=0&page=1&mode=s&remoteWork=&keyword=%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90%E5%B8%AB&jobsource=n104bank1"
res=requests.get(url,headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
# work_title_html = soup.select('div[class="b-block__left"]')
work_title_html = soup.find_all('article',class_='js-job-item')
print(work_title_html)

fn = '台北市104資料分析師職缺1.csv'
columns_name=['職務名稱','公司名稱','區域','薪資','工作內容']
with open(fn, 'w', newline='', ) as csvFile:
    dictwriter = csv.DictWriter(csvFile, fieldnames=columns_name)
    dictwriter.writeheader()
    for each_article in work_title_html:
        print(each_article.select("a"))
        print(each_article.find("a",class_="js-job-link").text)
        print(each_article.get('data-cust-name'))
        print(each_article.find('ul',class_='job-list-intro').find('li').text)
        print(each_article.select("p"))

        job_name = each_article.find("a", class_="js-job-link").text                 # 職務名稱
        company_name=each_article.get('data-cust-name')                              #公司名稱
        company_area=each_article.find('ul',class_='job-list-intro').find('li').text #區域
        Salary=each_article.find('span',class_='b-tag--default').text                #薪資
        work_content=each_article.find("p")                                          #工作內容
        dictwriter.writerow({'職務名稱': job_name, '公司名稱': company_name, '區域': company_area, '薪資': Salary, '工作內容': work_content})
