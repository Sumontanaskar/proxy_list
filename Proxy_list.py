import urllib2
from bs4 import BeautifulSoup
import base64

url = 'https://proxy-list.org/english/index.php'

k = []

def f_write(output):
    f = open('p_list.txt', "a+")
    f.write(output)
    f.close()

def ip_conv(coded_string):
    s = coded_string[6:-2]
    ip = base64.b64decode(s)
    return ip+':'

print 'Collecting data for:', url
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, "html5lib")
output = soup.select("div.table-wrap div.table ul li")
for list in output:
    k = list.find(text=True)
    k = str(k)+':'
    if k[0:5] == 'Proxy':
        k = ip_conv(k)
    if len(k) != 24:
        f_write(k)
    else:
        f_write('\n')
