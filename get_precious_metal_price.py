import sys
import urllib2
import re
import time

target_list = ["Gold", "Silver", "Platinum"]
while True :
    timer = int(time.time()) 
    if timer % 60 == 0 :
        url = "http://m.kitco.com"
        wp = urllib2.urlopen(url)
        content = wp.read().replace("\r","").replace("\n", "").replace("\t","")
        fp = open("/root/collection/web2.txt","w+")
        fp.write(content)
        fp.close()
        #print "target website: " + wp.geturl()
        price_list = []
        for target in target_list:
            regexp = target + r'</a></td>\s*<td\s*nowrap=\"nowrap\">[0-9]+\.[0-9]+</td>'
            #regexp = r'<td\s*nowrap=\"nowrap\">[0-9]+\.[0-9]+</td>'
            print regexp
            pattern = re.compile(r'' + regexp + '')
            matched = pattern.search(content)
            #print matched
            price = re.search(r"[0-9]+\.[0-9]+", matched.group(0))
            price_list.append(price.group(0))
        record = str(timer) + "," + ",".join(price_list) + "\n"
        fp = open("/root/collection/pmetal_price.dat","a+")
        fp.write(record)
        fp.close()

