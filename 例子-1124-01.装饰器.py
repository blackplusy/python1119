#coding=utf-8
import time
#计算一个函数的运行时间
def jisuan(func):
	def zsq():
		starttime=time.time()
		func()
		endtime=time.time()
		sec=endtime-starttime
		print('消耗的时间为%d'%sec)
	return zsq
@jisuan
def func():
	print('hello')
	time.sleep(1)
	print('world')

#func()
f=func
f()



