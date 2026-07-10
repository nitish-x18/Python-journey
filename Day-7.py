# store student names and marks in a dictionary, compute average, highest and lowest print a formate report--->

"""details = {}
n = int(input("enter dictionary items: "))

for i in range(n):
    names = input("enter your name: ")
    marks = input("enter your marks: ")
    details[names] = marks

print(details)"""

# OOPS--->
# OBJECT ORIENTED PROGRAMMING 

# CLASSES - BLUEPRINTA
# OBJECTS = REAL THINGS CREATED FROM BLUEPRINTS

# PASS STATMENT---
# CLASS HOUSE:
#     PASS

#CUNSTRUCTOR--->
#__INIT__()

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

student1 = student("nitish",20)
student1.name = "abc"
print(student1.name)


class math:
    def add(self,a,b):
        return a+b
    
    def multiply(self,a,b):
        return a*b
    
calc = math()
r1 = calc.add(1,2)
r2 = calc.multiply(1,2)

print(r1)
print(r2)

#INHERITANCE---->

class A:
    def hello(self):
        print("hello form class a")

class B(A):
    def hii(self):
        print("hii from class b")

a1 = B()
a1.hello() # call metrhod from class A
a1.hii() # call metrhod from class B

# ENCAPSULATI0N--->
class ab:
    def __init__(self,name,age):
        self.__name = name #private attribute
        self.age = age

    def test(self):
        return self.__name

ab1 = ab("a",1)
print(ab1.test())
print(ab1.age)

#POLYMORPHISM--->
class dog:
    def sound(self):
        print("wofff!")

class cat:
    def sound(self):
        print("meow")

class cow:
    def sound(self):
        print("mooo")

dog1 = dog()
cat1 = cat()
cow1 = cow()

dog1.sound()
cat1.sound()
cow1.sound()