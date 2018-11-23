#coding=utf-8
#a=20
#b=10
#print(a+b)
#a='heygor '
#b='shuai'
#print(a+b)
class animal:
	def jiao(self):
		print('ao~~~~~~')

class dog(animal):
	def jiao(self):
		print('汪！！！！')
class cat(animal):
	def jiao(self):
		print('miao~~~~~')

def test(s):
	s.jiao()

a=animal()
a.jiao()
b=dog()
c=cat()
test(b)
test(c)







