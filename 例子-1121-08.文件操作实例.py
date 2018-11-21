#coding=utf-8
file=open('/home/heygor/1121/txl.txt','r')
for i in file.readlines():
	#print(i)
	#print(type(i))
	i=i.strip('\n')
	b=i.split(' ')
	print(b)
	if b[-1]=='18888888888':
		print('tel is here!')
file.close()


