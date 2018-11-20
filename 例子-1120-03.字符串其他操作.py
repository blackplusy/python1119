#coding=utf-8
#拼接
a='python'

b=' no.1'

print(a+b)

print(a+b[-1])
#遍历

for i in a:
	print(i)

#成员运算
if 'p' in a:
	print('p is here!')

print('----------------')
#去空格
str1='   python  '
print(str1.strip())	#去掉左右空格
print(str1.lstrip())	#去掉左边空格
print(str1.rstrip())	#去掉右边空格

#计算长度
print(len(str1))












