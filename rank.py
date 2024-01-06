import requests
import random
from bs4 import BeautifulSoup
import pandas as pd
import datetime

# inputs
keyword = 'houses for sale in california'
sitename = "https://www.realtor.com/"
device = 'Desktop'

competitor1 = "https://www.zillow.com"
competitor2 = "https://www.homes.com"
competitor3 = "https://www.redfin.com"

competitors = [competitor1,competitor2,competitor3]


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


def clean_url(url):
    """
   Cleans a given URL by extracting the portion starting from 'https://'
   up to the '&ved' parameter, if present.

   Parameters:
   url (str): The URL to be cleaned.

   Returns:
   str: The cleaned URL or None if 'https://' is not found.
   """
    # Find the start of 'https://'
    start = url.find('https://')
    if start == -1:
        return None  # 'https://' not found in the URL

    # Find the end position, which is the start of '&ved'
    end = url.find('&ved', start)
    if end == -1:
        # If '&ved' is not found, return the URL from 'https://' onwards
        return url[start:]
    else:
        # Return the URL from 'https://' up to '&ved'
        return url[start:end]
    
def rank_check(sitename,serp_df,keyword,type):
        counter = 0
        #here is where we count and find our url
        d=[]
        for i in serp_df['URLs']:
            counter = counter + 1
            if sitename in str(i):
                rank = "%d" % (counter)
                url = i 
                now = datetime.date.today().strftime("%d-%m-%Y")
                d.append([keyword,rank,url,now,type])
                print(keyword,rank,url, now)
                
        df = pd.DataFrame(d)
        df['Rank'] = df['Rank'].astype(int)
        
        df.columns = ['Keyword', 'Rank', 'URLs','Date','Type']
                
        return df
                

def get_data(keyword,sitename,headers):
    # Google Search URL
    google_url = 'https://www.google.com/search?num=100&q='
    
    #checking what device we are checking
    if device.lower() == 'mobile':
        print('Using Mobile UserAgent')
        useragent = random.choice(mobile_agent)      
        headers = {'User-Agent': useragent}
        
    elif device.lower() ==' desktop':
        print('Using Desktop UserAgent')
        useragent = random.choice(desktop_agent)      
        headers = {'User-Agent': useragent}
        

    # Make the request
    response = requests.get(google_url + keyword, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        print('True')
        # Parse the content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        if device.lower() == 'mobile':
            # Find search results
            #titles = soup.find_all('h3', limit=10)
            #div 
            print('mobile')
            urls = soup.find_all('div', class_="KJDcUb")

        elif device.lower() == 'desktop':
            urls = soup.find_all('div', class_="egMi0")
            
        
        
        data= []
        for div in urls:
            print(div)
            soup = BeautifulSoup(str(div), 'html.parser')
        
            # Extracting the URL
            url_anchor = soup.find('a')
            url = url_anchor['href'] if url_anchor else "No URL"
            
            url = clean_url(url)
        
            data.append(url)
            
        serp_df = pd.DataFrame(data,columns =['URLs'])
        
        results = rank_check(sitename,serp_df,keyword,"My Site")
    
        #competiors
        for competitor in competitors:
            print(competitor)
            c = rank_check(competitor,serp_df,keyword, "Competitor")
            results = pd.concat([results, c])
            print(c)      
            
            df = pd.DataFrame(results).sort_values(by='Rank')
            
        return df
   



KJDcUb
                
df = get_data(keyword,sitename,headers)              
                
              
    