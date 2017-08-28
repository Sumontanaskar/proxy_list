import urllib2
from bs4 import BeautifulSoup
import base64
import os
output_file = 'proxychains.conf'
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


file =open('p_list.txt', "r")
with open(output_file, "wb") as f:
    f.seek(999999)
    f.write("\0")

str='''
dynamic_chain
proxy_dns
tcp_read_time_out 15000
tcp_connect_time_out 8000
[ProxyList]
    '''
f = open(output_file, "a+")
f.write(str)
for list in file:
    data = list.split(':')
    k = data[2]+'\t'+data[0]+'\t'+data[1]+'\n'
    f.write(k)
    print k
f.close()
file.close()
os.remove('p_list.txt')