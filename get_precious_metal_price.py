import sys
import urllib2
import re
import time
import psycopg2

target_list = ["Gold", "Silver", "Platinum"]
conn = psycopg2.connect(database="test", user="root", password="d&kdz555", host="localhost", port="5432");
cur = conn.cursor()
cur.execute("SELECT MAX(id)+1 FROM price_precious_metal")
id = cur.fetchall()[0][0] or 1

while True :
    timer = int(time.time()) 
    if timer % 60 == 0 :
        url = "http://m.kitco.com"
        wp = urllib2.urlopen(url)
        content = wp.read().replace("\r","").replace("\n", "").replace("\t","")
#        fp = open("/root/collection/web2.txt","w+")
#        fp.write(content)
#        fp.close()
#        print "target website: " + wp.geturl()
        price_list = []
        for target in target_list:
            regexp = target + r'</a></td>\s*<td\s*nowrap=\"nowrap\">[0-9]+\.[0-9]+</td>'
#            print regexp
            pattern = re.compile(r'' + regexp + '')
            matched = pattern.search(content)
            #print matched
            price = re.search(r"[0-9]+\.[0-9]+", matched.group(0))
            price_list.append(str(float(price.group(0)) * 100))
        record = str(timer) + "," + ",".join(price_list)
#        fp = open("/root/collection/pmetal_price.dat","a+")
#        fp.write(record)
#        fp.close()
        sql = "INSERT INTO price_precious_metal (id,bid_time,gold_price,silver_price,platinum_price) VALUES (" + str(id) + "," + record + ")"
        print sql
        cur.execute(sql)
        conn.commit()
        id = id + 1
