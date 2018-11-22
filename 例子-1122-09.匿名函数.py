#coding=utf-8
sum=lambda a1,a2:a1+a2
print('相加后的值是',sum(10,20))

#例子：字典排序
stu=[{'name':'pig','age':18},{'name':'dog','age':3},{'name':'cat','age':30}]
stu.sort(key=lambda x:x['age'])
print(stu)

#例子：把lambda当作一个变量
def operation(a,b,opt):
	re=opt(a,b)
	return re

num1=int(input('num1:'))
num2=int(input('num2:'))
res=operation(num1,num2,lambda a,b:a+b)
print(res)

