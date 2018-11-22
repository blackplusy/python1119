def animal(pet1,pet2):
	print(pet1+' wang!'+pet2+' miao')

#调用函数传入两个参数
animal('dog','cat')

def animal(pet1,pet2):
	print(pet1+' wang!'+pet2+' miao')

animal(pet2='cat',pet1='dog')

def animal(pet2,pet1='2ha'):
	print(pet1+' wang!'+pet2+' miao')

animal('bosi')
animal('pig','out man')

print('************************************')
def test(x,y,*args):
	print(x,y,args)

test(1,2,'heygor','simida')

print('************************************')
def test1(x,y,**args):
	print(x,y,args)

test1(1,2,a=9,b='heygor',c=300)




