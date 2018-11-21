#coding=utf-8
import csv

with open('/home/heygor/2.csv','w') as f:
	file=csv.writer(f,dialect='excel')
	file.writerow([1,2,3,4])
	file.writerow([5,6,7,8])
