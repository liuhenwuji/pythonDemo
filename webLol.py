# -*- coding: UTF-8 -*-
import requests
import bs4

# response = requests.get('http://www.qtfy.cc/ysyl/26466.html')
# response = requests.get('http://www.loldytt.com/Dianshiju/NHJSG/')
response = requests.get('http://www.qtfy.cc/ysyl/28180.html')
# response = requests.get('http://www.loldytt.com/Dianshiju/WXFS2/')
# response = requests.get('http://www.loldytt.com/Dianshiju/WXFS2')

soup = bs4.BeautifulSoup(response.text, 'html.parser')
links = soup.find_all("input")
# print(response.text)
links = soup.find_all("a", href=True)
count = 0
for link in links:
    url = link.get("href")
    if url.startswith('thunder') or url.startswith('ed2k'):
        print(url)
        count = count + 1
print(count)
print()

count = 0
for link in links:
    url = link.get("href")
    if url.startswith('magnet'):
        print(url)
        count = count + 1
print(count)

# print(links)
