#!/usr/bin/env python
# -*-coding:utf-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import re
import pymysql.cursors

url="https://hao.360.cn/";
req=request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')

resp=request.urlopen(url).read().decode('utf-8')
soup=BeautifulSoup(resp,"html.parser")
listurls = soup.findAll('a',href=re.compile('^https'))
for url in listurls:
	print(url.get_text().strip(),url['href'])

	connection=pymysql.connect(host='localhost',user='root',password='',db='wikiurl',charset='utf8mb4')

	try:
		with connection.cursor() as cursor:
			sql='insert into`urls`(`urlname`,`urlref`)values(%s,%s)'
			cursor.execute(sql,(url.get_text().strip(),url['href']))
			connection.commit()

	finally:
		connection.close()

#print(listurls)