#coding=utf-8
a=100
print('a的值是',a)

def test1():
	global a
	a=200
	print('test1中修改全局变量a',a)

def test2():
	print('test2中使用全局变量a',a)

test1()
test2()
