#coding:utf-8
import urllib
import urllib2
from bs4 import BeautifulSoup
import re,socket,time,threading

def makeurl(a,b):
    my_url=[]    
    for pagenum in range(a,b):
        URL='http://www.meizitu.com/a/'+str(pagenum)+'.html'
        my_url.append(URL)
    return my_url

class getUrls(threading.Thread):
    def __init__(self,url):
        self.url=url
        threading.Thread.__init__(self)
    def run(self):       
        try:
            req=urllib2.Request(self.url)
            response=urllib2.urlopen(req,timeout=60)
            page=response.read()
            response.close()
            regex=re.compile(r'http://pic.meizitu.com/wp-content/uploads/.*?\.jpg',re.S)
            soup=BeautifulSoup(page)
            items=soup.find_all('img',attrs={'src':regex})
            jpg=[]
            names=[]
            for item in items:
                print item['src']
                print item['alt']
                filename=item['alt']+'.jpg'
                urllib.urlretrieve(item['src'], filename)
        except IOError as e:
                print '----IOError url:',url
        except urllib2.URLError as e:
                print '----urlError url:',url
        except socket.timeout as e:
                print '----socket timeout:',url

my_url_1=makeurl(5400,5500)
my_url_2=makeurl(5500,5700)
my_url_3=makeurl(5000,5100)   
my_url_4=makeurl(5200,5300)
for url in my_url_1:
    thread1=getUrls(url)
    thread1.start()
for url in my_url_2:
    thread2=getUrls(url)
    thread2.start()
# for url in my_url_3:
#     thread3=getUrls(url)
#     thread3.start()
# for url in my_url_4:
#     thread4=getUrls(url)
#     thread4.start()       
     



