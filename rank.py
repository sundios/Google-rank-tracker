import sys
import re
import random
from random import randint
from robobrowser import RoboBrowser
import datetime
import csv
import pandas as pd
import time

#Terminal arguments to pass when running the script
sitename = sys.argv[1]
device = sys.argv[2]
#keyword = "+".join(sys.argv[3:])

#printing the arguments before script starts 
#print("site: %s keyword: %s device: %s"  % (sitename, keyword , device))


#Mobile user agent strings found on https://deviceatlas.com/blog/mobile-browser-user-agent-strings
mobile_agent = [
#Safari for iOS
'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
#Android Browser
'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
#Chrome Mobile
'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36',
#Firefox for Android
'Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0',
#Firefox for iOS
'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) FxiOS/7.5b3349 Mobile/14F89 Safari/603.2.4',
#Samsung Browser
'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G955U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.4 Chrome/51.0.2704.106 Mobile Safari/537.36',
]

# desktop user agent strings. Source: https://deviceatlas.com/blog/list-of-user-agent-strings
desktop_agent = [
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


#Creating Mobile function with 4 arguments.
"""
keyword: Keyword that we are checking that comes from keywords.xls
sitename: the URL we want to chekc against. Its define when we run the script
device: Mobile or desktop. Its define when we run the script
useragent: selected randomly from list when we know device.
"""
def mobile(keyword,sitename,device,useragent):
    parser = 'html.parser'
 
    browser = RoboBrowser(history=False,
                          user_agent=useragent,
                          parser=parser)
     
    browser.open('https://www.google.com/search?num=100&q=' + keyword)
    
    #this is the div that only shows up on mobile device. This might change not sure :/ 
    links = browser.find_all("div", {"class": "KJDcUb"})

    # links = browser.find_all("div", {"class": "g"})
     
    counter = 0


    print('The user Agent you used was ----> ' + useragent)

    #here is where we count and find our url
    d=[]
    for i in links:
        counter = counter + 1
        if sitename in str(i):
            url = i.find_all('a', href=True)
            position = "%d" % (counter)
            rank = "%s" % (url[0]['href'])
            now = datetime.date.today().strftime("%d-%m-%Y")
            keyword = keyword
            device = device
            d.append(keyword)
            d.append(position)
            d.append(rank)
            d.append(device)
            d.append(now)
            print(keyword, position, rank, device, now)
    
    #invoking csv export function 
    csv_export(d,keyword,device)

#desktop function. Exactly the same as mobile with the difference of div that we look for our URLs
def desktop(keyword,sitename,device,useragent):
    parser = 'html.parser'
 
    browser = RoboBrowser(history=False,
                          user_agent=useragent,
                          parser=parser)
     
    browser.open('https://www.google.com/search?num=100&q=' + keyword)
     
    # links = browser.find_all("div", {"class": "KJDcUb"})

    #desktop div where URLs are
    links = browser.find_all("div", {"class": "g"})
     
    counter = 0

    print('The user Agent you used was ----> ' + useragent)

    d=[]
    for i in links:
        counter = counter + 1
        if sitename in str(i):
            url = i.find_all('a', href=True)
            position = "%d" % (counter)
            rank = "%s" % (url[0]['href'])
            now = datetime.date.today().strftime("%d-%m-%Y")
            keyword = keyword
            device = device
            d.append(keyword)
            d.append(position)
            d.append(rank)
            d.append(device)
            d.append(now)
            print(keyword, position, rank, device, now)
    
    csv_export(d,keyword,device)

#function to export to csv file.

"""
d: Is the complete dataframe we generate on our mobile() or desktop() functions with all the important data
keyword: Keyword we run. We need this only to add it to the name of the csv
device: device we checked. We need this only to add it to the name of csv.
"""
def csv_export(d,keyword,device):
    file =datetime.date.today().strftime("%d-%m-%Y")+'-' +keyword + '-' + device +'.csv'
    with open(file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Keyword' , 'Rank', 'URL' ,'Device', 'Date'])
        writer.writerows(zip( d[0::5], d[1::5] , d[2::5], d[3::5] , d[4::5]))


#Keyword file
keywords = pd.read_excel('keywords.xls')

#user agent checker. Here depending on what the user agent was passed in th sys arguments we perform diferent functions.
if device == 'mobile' :
    useragent = random.choice(mobile_agent)
    print('Using mobile device')  
    for keyword in keywords['Keywords']:
        print(keyword)
        mobile(keyword,sitename,device,useragent)
        t = randint(1,10)
        print('Sleeping time is' ,t ,'Seconds')
        time.sleep(t)
   
  
elif device == 'desktop':
    print('Using desktop device')
    useragent = random.choice(desktop_agent)
    for keyword in keywords['Keywords']:
        print(keyword)
        desktop(keyword,sitename,device,useragent)
        t = randint(1,10)
        print('Sleeping time is' ,t ,'Seconds')
        time.sleep(t)
else:
    print(" X_X You didn't specify a user agent. We will still run the script but your filename will have a weird name")
    useragent = random.choice(mobile_agent)
    for keyword in keywords['Keywords']:
        print(keyword)
        mobile(keyword,sitename,device,useragent)
        t = randint(1,10)
        print('Sleeping time is' ,t ,'Seconds')
        time.sleep(t)













