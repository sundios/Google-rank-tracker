import sys
import re
import random
from robobrowser import RoboBrowser
import datetime
import csv



sitename = sys.argv[1]
keyword = "+".join(sys.argv[2:])
 
print("site: %s keyword: %s" % (sitename, keyword))
 
agent = [
## Chrome 60 Windows
'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
## Firefox 36 Windows
'Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0',
### Chrome 67 Windows
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
### Chrome 79 Windows 
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
### Webkit MacOs
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko)',
### Chrome 79 MacOS
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
## FireFox Generic MacOS
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0']

 
parser = 'html.parser'

useragent = random.choice(agent)
 
browser = RoboBrowser(history=False,
                      user_agent=useragent,
                      parser=parser)
 
browser.open('https://www.google.com/search?num=100&q=' + keyword)
 
links = browser.find_all("div", {"class": "g"})
 
counter = 0

# print('The user Agent you used was ----> ' + useragent)

d=[]
for i in links:
    counter = counter + 1
    if sitename in str(i):
        url = i.find_all('a', href=True)
        position = "%d" % (counter)
        rank = "%s" % (url[0]['href'])
        now = datetime.date.today().strftime("%d-%m-%Y")
        keyword = keyword
        d.append(keyword)
        d.append(position)
        d.append(rank)
        d.append(now)
        print(keyword, position, rank, now)



file =datetime.date.today().strftime("%d-%m-%Y")+'-' +keyword + '.csv'
with open(file, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Keyword' , 'Rank', 'URL' , 'Date'])
    writer.writerows(zip( d[0::4], d[1::4] , d[2::4], d[3::4]))