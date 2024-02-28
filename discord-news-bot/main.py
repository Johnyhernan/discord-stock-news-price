import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
import time
import datetime
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/61.0.3163.79 Chrome/61.0.3163.79 Safari/537.36'}
def getPrice(stock):
    url= 'https://finance.yahoo.com/quote/'+stock+'?p='+stock+'&.tsrc=fin-srch'

    r= requests.get(url,headers=headers)
    soup= BeautifulSoup(r.text,'lxml')
    hada= soup.find_all('div',{'class':'D(ib) Mend(20px)' })
    '''getting current price'''
    price= soup.find('fin-streamer',{'class':'Fw(b) Fz(36px) Mb(-4px) D(ib)' })
    for span in price:
        b=(span.text)
    '''getting current price change'''
    priceChange=soup.find('fin-streamer',{'class':'Fw(500) Pstart(8px) Fz(24px)' })

    for span in priceChange:
        a=(span.text)
    '''getting after hours/ pre market: price'''
    after=soup.find('fin-streamer',{'class':'C($primaryColor) Fz(24px) Fw(b)' })
    for span in after:
        ah=(span.text)
    '''getting current volume'''
    volume=soup.find('fin-streamer',{'data-field':'regularMarketVolume' })
    for span in volume:
        vol=(span.text)

        
    time=datetime.datetime.now()
    time=time.strftime('%Y-%m-%d')

    ab=[]
    ab.append(stock)
    ab.append(time)
    ab.append(a)
    ab.append(b)
    ab.append(vol)
    ab.append(ah)

    '''sending info  to discord bot'''
    return ab

def getData(stock):
    url= 'https://finviz.com/quote.ashx?t='+stock+'&p=w'

    r= requests.get(url,headers=headers)
    soup= BeautifulSoup(r.text,'lxml')
    hada= soup.find_all('div',{'class':'news-link-container' })
    nada= soup.find_all('table',{'class':'news-table' })
    temp='a'
    count=0
    news=[]

    '''getting current news headline'''
    for a in hada:
        
        news.append(a.text.replace('\n', ''))

       

        
        


    return news

