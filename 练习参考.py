#coding=utf-8

dic={'heygor':'123','baigor':'456'}

while 1:
	name=input('请输入您的用户名：')

	if len(name)==0:
		print('您输入的用户名为空')
	elif name in dic.keys():
		print('没问题！')
		while 1:
			passwd=input('请输入您的密码：')
			if passwd ==dic[name]:
				print('登录成功')
				break
			else:
				print('请重新输入密码')			

	else:
		print('您的用户名有问题')
