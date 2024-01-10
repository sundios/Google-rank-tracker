import requests
import random
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import threading
from halo import Halo
from termcolor import colored

# Set up the spinner animation
spinner = Halo(text='', spinner='dots')
# Start the spinner
spinner.start()

# inputs
keyword = 'running shoes'
sitename = "https://www.adidas.com/"

competitor1 = "https://www.nike.com"
competitor2 = "https://www.reebok.com"
competitor3 = "https://www.ascics.com"
competitor4 = "https://www.hoka.com"


competitors = [competitor1,competitor2,competitor3, competitor4]


#Mobile user agent strings f
mobile_agent = [
    # Safari for iOS
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1',
    
    # Chrome for iOS
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.5735.99 Mobile/15E148 Safari/604.1',
    
    # Firefox for iOS
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/114.1 Mobile/15E148 Safari/605.1.15',
    
    # Microsoft Edge for iOS
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 EdgiOS/114.0.5735.99',

]

desktop_agent = [
    # Updated Chrome 110 on Windows
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    
    # Updated Chrome 110 on MacOS
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    
    # Updated Firefox 105 on MacOS
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0',
    

    # Updated Safari 15 on MacOS
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:15.0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15',

 ]





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
            counter += 1
            if sitename in str(i):
                rank = counter
                url = i 
                now = datetime.date.today().strftime("%d-%m-%Y")
                d.append([keyword,rank,url,now,type])
                #print(keyword,rank,url, now)
                
        df = pd.DataFrame(d)
       
        
        if d:  # Check if the list 'd' is not empty
            df = pd.DataFrame(d)
            df.columns = ['Keyword', 'Rank', 'URLs', 'Date', 'Type']
        else:
            # Create an empty DataFrame with the specified columns
            df = pd.DataFrame(columns=['Keyword', 'Rank', 'URLs', 'Date', 'Type'])

        return df
                

def get_data(keyword,sitename,device):
    
    
    
    # Google Search URL
    google_url = 'https://www.google.com/search?num=100&q='
    
    #checking what device we are checking
    if device.lower() == 'mobile':
        print(colored("- Checking Mobile Rankings" ,'black',attrs=['bold']))
        useragent = random.choice(mobile_agent)      
        headers = {'User-Agent': useragent}
        print(headers)
        
    elif device.lower() =='desktop':
        print(colored("- Checking Mobile Desktop" ,'black',attrs=['bold']))
        useragent = random.choice(desktop_agent)      
        headers = {'User-Agent': useragent}
        print(headers)
        

    # Make the request
    response = requests.get(google_url + keyword, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        if device.lower() == 'mobile':
            # Find search results
            #titles = soup.find_all('h3', limit=10)
            urls = soup.find_all('div', class_="P8ujBc")
            
        elif device.lower() == 'desktop':
            urls = soup.find_all('div', class_="yuRUbf")
    
        data= []
        for div in urls:
            soup = BeautifulSoup(str(div), 'html.parser')
           
            # Extracting the URL
            url_anchor = soup.find('a')
            if url_anchor:
                url = url_anchor.get('href', "No URL")
            else:
                url = "No URL"
            
            url = clean_url(url)
        
            data.append(url)
            
        serp_df = pd.DataFrame(data,columns =['URLs'])
        serp_df = serp_df.dropna(subset=['URLs'])
        
        results = rank_check(sitename,serp_df,keyword,"My Site")
        
        print(colored(f"- Ranking results for {sitename}",'black',attrs=['bold']))
        print(results)
    
        #competiors
        for competitor in competitors:
            c = rank_check(competitor,serp_df,keyword, "Competitor")
            results = pd.concat([results, c])
            

        df = pd.DataFrame(results)
        
        df = df.sort_values(by='Rank')
            
    elif response.status_code == 429:
        # Handle rate limiting
        print('Rate limit hit, status code 429. You are Blocked From Google')
        error_message = 'Rate limit hit, status code 429. You are Blocked From Google'
        df = pd.DataFrame({'status': [error_message]})
    else:
        # Handle other status codes
        print(f'Failed to retrieve data, status code: {response.status_code}')
        error_message = f'Failed to retrieve data, status code: {response.status_code}'
        df = pd.DataFrame({'status': [error_message]})
        
    print(colored(f"- Competitors Ranking results",'black',attrs=['bold']))   
    print(df)   
    
    return df

                
mobile = get_data(keyword,sitename,'mobile')
import time

# Wait for 5 seconds
time.sleep(5)
#desktop = get_data(keyword,sitename,'desktop')          
                


# try:
#     with pd.ExcelWriter(f"{keyword}.xlsx", engine='openpyxl') as writer:
        
#         # Write each DataFrame to a different worksheet
#         desktop.to_excel(writer, sheet_name='Desktop')
#         mobile.to_excel(writer, sheet_name='Mobile')
#     pass
# except Exception:
#     print('No Data, please try again')
    
# Stop the spinner
spinner.stop_and_persist(symbol='🤖'.encode('utf-8'), text='All Checks have been finalized!')

              

    