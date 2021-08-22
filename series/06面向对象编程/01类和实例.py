"""
面向对象编程
面向对象编程简称OOP，是一种程序设计思想，OOP把程序的基本单元，一个对象包含了数据和操作数据的函数
面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。
而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。
在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。
"""
# 我们以一个例子来说明面向过程和面向对象在程序流程上的不同之处。
# 假设我们要处理学生的成绩表，为了表示一个学生的成绩，面向过程的程序可以用一个dict表示：
std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Bob', 'score': 81}


# 而处理学生成绩可以通过函数实现，比如打印学生的成绩：
def print_score(std):
    print('%s: %s' % (std['name'], std['score']))


"""
如果采用面向对象的程序设计思想，我们首选思考的不是程序的执行流程，而是Student这种数据类型应该被视为一个对象，
这个对象拥有name和score这两个属性（Property）。如果要打印一个学生的成绩，首先必须创建出这个学生对应的对象，
然后，给对象发一个print_score消息，让对象自己把自己的数据打印出来。
"""

# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))


# 给对象发消息实际上就是调用对象对应的关联函数，我们称之为对象的方法（Method）。面向对象的程序写出来就像这样：
# bart = Student('Bart Simpson', 59)
# lisa = Student('Lisa Simpson', 87)
# bart.print_score()
# lisa.print_score()

# 面向对象的设计思想是从自然界中来的，因为在自然界中，类（Class）和实例（Instance）的概念是很自然的。
# Class是一种抽象概念，比如我们定义的Class——Student，是指学生这个概念，而实例（Instance）则是一个个具体的Student，比如，Bart Simpson和Lisa Simpson是两个具体的Student。

# 所以，面向对象的设计思想是抽象出Class，根据Class创建Instance。
# 面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法。


"""
类和实例
面向对象最重要的概念就是类(Class)和实例(Instance)，必须牢记类是抽象的模板，比如Student类，而实例就是根据类创建出来的一个一个具体的对象
每个对象都拥有相同的方法，但各自数据可能不同

"""


# 仍然以Student类为例，在Python中定义类是通过class关键字
class Studnet(object):
    pass


# class后面是类名，即Student，类名通常是大写开头的单词
# 紧接着是(object)，表示该类是从哪个类继承而来的，通常，如果没有合适的继承类，就是用object剋，这是所有类最终都会继承的类

# 定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的
bart = Studnet()  # <__main__.Studnet object at 0x000001FC6F159FD0>
print(bart)

# 可以看到变量bart指向的就是一个Student的实例，后面的0x000001FC6F159FD0就是内存地址，每个object的地址都不一样，而Student本身就是一个类。
# 可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性：
bart.name = "Bart Simpson"
print(bart.name)


# 由于类可以起到模板的作用，可以在创建实例的使用，把我们一些认为必须绑定的属性强制填写进去
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑定上去
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


# 注意：特殊方法__init__前后分别有两个下划线
# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。

# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：

bart = Student("Bart Simpson", 60)
print(bart.name)
print(bart.score)

# 和普通函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用的时候
# 不需要传递该参数，除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可选参数、关键字参数、命名关键字参数


"""
数据封装
面向对象编程的一个重要特点就是数据封装，在上面的Student类中，每个实例就拥有各自的name和hscore这些数据
我们可以通过函数来访问这些数据，比如打印一个学生的成绩
"""


def print_score(std):
    print("%s: %s" % (std.name, std.score))


print_score(bart)


# 但是，既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，

# 可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法：
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


andrew = Student("Andrew", 20)
# 要定义一个方法，除了第一个参数是self外，其他和普通函数一样。要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入：
andrew.print_score()


# 这样一来，我们从外部看Student类，就只需要知道，创建实例需要给出name和score，而如何打印，都是在Student类的内部定义的，
# 这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节。

# 封装的另一个好处是可以给Student类增加新的方法，比如get_grade：
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


# 同样的，get_grade方法可以直接在实例变量上调用，不需要知道内部实现细节：
andrew = Student("Andrew", 20)
andrew.print_score()
print(andrew.get_grade())


"""
类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

>>> bart = Student('Bart Simpson', 59)
>>> lisa = Student('Lisa Simpson', 87)
>>> bart.age = 8
>>> bart.age
8
>>> lisa.age
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'age'

"""