import requests
from bs4 import BeautifulSoup
import time
import codecs
import pandas as pd

companies = []

for x in range(2,6):
    url = 'https://www.visalietuva.lt/en/companies/gates/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/94.0.4606.71 Safari/537.36 '
    }

    ''' request data '''
    r = requests.get(url+str(x), headers= headers)


    ''' parsing html file with beautifulsoup4 '''
    soup = BeautifulSoup(r.text, 'html.parser')


    '''creating/download to local html file'''
    #f = open('./res.html', 'wb')
    #f.write(r.content)
    #f.close()

    ''' open/read local html file '''
    #file = codecs.open('res.html', 'r', 'utf-8')
    #info = file.read()
    #soup = BeautifulSoup(info, 'html.parser')

    contents = soup.find_all('div', {'class': 'item'})
    for content in contents:
        title = content.find('a', {'class': 'company-item-title'}).text
        streetaddress = content.find('span', {'itemprop': 'streetAddress'}).text
        localaddress = content.find('span', {'itemprop': 'addressLocality'}).text
        phone = content.find('div', {'class': 'col contacts'}).find_all('div')[5].text
        try:
            email = content.find('div', {'class': 'col contacts'}).find_all('div')[8].text
        except:
            pass

        companies_info= {
            'title': title,
            'streetaddress': streetaddress,
            'localaddress': localaddress,
            'phone': phone,
            'email': email
        }
        companies.append(companies_info)
    print('companies found : ', len(companies))
    time.sleep(3)

df = pd.DataFrame(companies)
print(df.head())

df.to_csv('companies.csv')
df.to_json('companies.json')
