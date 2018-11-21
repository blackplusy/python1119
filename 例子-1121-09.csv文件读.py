#coding=utf-8

import csv

with open('/home/heygor/1.csv','r') as f:
	reader=csv.reader(f)
	for i in reader:
		print(i)
