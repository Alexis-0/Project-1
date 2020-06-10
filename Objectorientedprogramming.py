class MyNewClass:# here the class name is MyNewClass
    a = 10# class contains a data number
    def func(self):# class contains a function
        print('hello')
ob = MyNewClass()# how to create an instance object named ob
print(ob.func())# obtaing func using the (ob.func())
print(ob.a)# obtaining func using the(ob .a)
ob1 = MyNewClass()# two objects were created from MyNewClass, ob1 and ob2
ob2 = MyNewClass()
print(ob1)
print(ob2)
ob1.a = 0
ob2.a = 100
print(MyNewClass.a)# python created a MyNewClass object and use it to access other info
class number: # the class is named number
    def add(self, a, b):# class has two functions add/multiply
        return a+b
    def multiply(self, a, b):# the first argument in a function must be self
        return a*b
n1 = number()#create an object n1 from the class called number
sum = n1.add(2, 3)
print(sum)
product = n1.multiply(2, 5)
print(product)
class MyClass:# instantiated objects o1 and o2 from MyClass
    def __init__(self,p1 = 0, p2 = 0):#__init__() initializes the variables
        self.a = p1# the self. is necessary,needs a variable name attached to object name=
        self.b = p2# the self. is necessary,
o1 = MyClass(2, 3)#object is instantiated using MyClass(2,3),__init__ is used automatically
print((o1.a, o1.b))# o1.a and o1.b have the values of 2 , 3 respectively
o2 = MyClass()#o2 objects are initialized with default values of 0
print((o2.a, o2.b))
class Point(object):
    def __init__(self, x = 0, y= 0):
        self.x = x
        self.y = y
    def distance(self):
        """Find distance from origin"""
        return (self.x**2 + self.y**2) **0.5
p1 = Point(6, 8)# created an object from p1 from point class, value of p1.x=6 and p1.y=8
distance = p1.distance()#called distance to calc distance from origin
#p1.distance = point.distance(p1).the object p1 is accepted by the self parameter. self.x=p1.x etc
del p1.y
print(p1.x)
#print(p1.y)
p1 = Point(6, 8)
del p1
#print(p1)
class BaseClass:
    #body of the base class
    pass
class DerivedClass(BaseClass):# inherits features from the base class, adding new features
    #Body of the derived class
    pass
class Polygon:
    def __init__(self, no_of_sides):# init func value all sides to 0, stores it in a sides list
        self.n = no_of_sides# self is mandatory as the first parameter
        self.sides = []# self parameter is used to reference the object itself
        for i in range(no_of_sides):
            self.sides.append(0)
    def input_sides(self):# takes n,number from user. updates the sides list with user entered values.
        for i in range(self.n):
            self.sides[i] = float(input('enter side' + str(i + 1) +':'))
    def display_sides(self):# displays these values
        for i in range(self.n):
            print('side', i +1, 'is', self.sides[i])
p1 = Polygon(3)
p1.input_sides()
p1.display_sides()
class Triangle(Polygon):#overriding a base method by calling the method in the baseclass from
    def __init__(self):#the one in the derived class
        Polygon.__init__(self, 3)
    def find_area(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        print('the area of the triangle is', area)
t =  Triangle()
t.input_sides()
t.find_area()
class Polygon:
    pass
class Triangle(Polygon):
    pass
t = Triangle()
print(isinstance(t, Triangle))
print(isinstance(t, Polygon))
print(isinstance(t, int))
print(isinstance(t, object))
print(issubclass(Polygon, Triangle))
print(issubclass(Triangle, Polygon))
a = 2# 2 is an object and a is the name we associate with it
print('id(2) =', id(2))
print(id(2))
print(id(a))# both a and 2 have the same id which means they refer to the same objects
a = a +1# a+1 becomes object 3 associated with a
b = 2# the new name b gets associated with 2
print(id(a))# id(a) and id(3) have the same value
print(id(3))
print(id(2))
object_1 = 5
object_1 = 'hello world'
object_1 = [1, 2, 3]
def printHello():
    print('hello')
object_1 = printHello
my_list_1 = [1, 4, 7]
list_statement = iter(my_list_1)#get an iterator using iter()
print(next(list_statement))
print(next(list_statement))
print(list_statement.__next__())#next(obj) is the same as obj.__next__()
#next(list_statement)
for num in my_list_1:
    print(num)
# how a for loop works in python
iterable = [45, 50, 55, 60]
iter_obj = iter(iterable)# create an iterator object
while True:#creates an infinte loop
    try:
        item = next(iter_obj)# next item
        print(item)
    except StopIteration:#terminate loop if StopIteration is raised
#    break:
        pass
class PowTwo:
    def __init__(self, max = 0):
        self.max = max
        def __init__(self):
            self.n = 0
            return self
        def __next__(self):
            if self.n <= self.max:
                result = 2 ** self.n
                self.n += 1
                return result
            else: raise StopIteration 
a = PowTwo(3)
i = iter(a)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
for i in powTwo(5):
    print(i)






