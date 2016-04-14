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
url = "http://m.kitco.com"
headers = [{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20151201 Firefox/3.5.6' }, {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}]

while True :
    timer = int(time.time()) 
    if timer % 60 == 0 :
        request = urllib2.Request(url = url, headers = headers[(timer%13)%2])
        wp = urllib2.urlopen(request)
        content = wp.read().replace("\r","").replace("\n", "").replace("\t","")
        price_list = []
        for target in target_list:
            regexp = target + r'</a></td>\s*<td\s*nowrap=\"nowrap\">[0-9]+\.[0-9]+</td>'
            pattern = re.compile(r'' + regexp + '')
            matched = pattern.search(content)
            price = re.search(r"[0-9]+\.[0-9]+", matched.group(0))
            price_list.append(str(float(price.group(0)) * 100))
        record = str(timer) + "," + ",".join(price_list)
        sql = "INSERT INTO price_precious_metal (id,bid_time,gold_price,silver_price,platinum_price) VALUES (" + str(id) + "," + record + ")"
        cur.execute(sql)
        conn.commit()
        id = id + 1
