学习目标
掌握self的应用

学习内容
a.self实例
b.注意事项

a.self实例
class student:
        def __init__(self,name):
                self.name=name
        def info(self):
                print('你的名字是%s'%self.name)

def studentinfo(s):
        s.info

heygor=student('ladygaga')
#heygor是student类的实例化对象
#对象实例化之后可以使用类的方法
studentinfo(heygor)
#studentinfo括号中传入的heygor是一个实例经历话的对象调用类的方法
注意：函数传参可以传入常规函数，也可以传入对象

b.注意事项
self可以理解为自己
可以把self当作c++类的指针一样理解，就是自己
当某个对象调用其方法时候python解释器会把这个对象作为第一个参数传递给self，开发者只需要传递后面参数即可

补充：在类中self只能在函数中使用，表示的是实例属性，每个实例可以设置不同的值，互相不影响
如果在类级别中没有使用self对的属性，是类属性，一般作为全局变量使用
