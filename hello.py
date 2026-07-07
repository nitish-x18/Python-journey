print("hello world!")

#functions--->
def test(a): #this a is parameter
    print(a)

test(5) #this 5 is positional arguments

def add(a,b):
    print(a+b)

add(a=2,b=2) #keyword argumemt

def user(name,age,place):
    print(f"My name is {name}, my age is {age}, and I am from {place}.")

user("nitish", age = 20, place = "chandigarh")

# *args--->
def hello(user,*abc):
    print(abc)
    print(user)
hello(1,2,3,"a","b","c")

# **kwargs--->
def hell(**abc):
    print(abc)
hell(a=1,b=2,c=3,d="absss")

def prac(regular,*abe,**abd):
    print(regular)
    for i in abe:
        print(i)
    print(abd)
prac(1,2,3,"a","b","c",a=7,b=8,c=9)

# globl and local scope--->

x = 10 # global variables
def val():
    e=20 # local variable
    print(e)
val() 

# lambda fumctions--->
# syntex of lambda function---> lambda parameters:experssions
addd = lambda a,b: a+b
print(addd(2,3))

func = lambda v,n,m:v*n*m
print(func(2,3,4))

def function(f,g,h):
    print(f*g*h)
    print(f"normal function")
print(function(2,3,4))

#lembda with conditional statments--->
numb = lambda x: "even" if (x%2 == 0) else "odd"
print(numb(3))

#to check which number is greter between two numbers--->
check = lambda a,b: f"{a} is greater number" if a>b else f"{b} is greater"
print(check(8,3))