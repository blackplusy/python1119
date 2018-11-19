#coding=utf-8
age=int(input('请输入您的年龄：'))

if  age>70:
	print('老年人')
else:
	print('年龄小于70')
	if age>0 and age<20:
		print('未成年！！')
	else:
		print('不要和我抢后裔！！')

