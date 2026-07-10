dict = {
    "firstvalue": [2,4,3,7,8,9,11,56,76],
    "secondvalue": (1,2,"hello")
}

# only print even number--->
even = [i for i in dict["firstvalue"] if i % 2 == 0]

#for i in dict["firstvalue"]:
 #   if i % 2 == 0:
   #     print(i)

print(even)

# print string number--->


# STRINGS---->
a = 'abc'
a = "abc"
a = """multi line strings"""

print(a[2])
print(a[1:3]) # slicing
print(a[::-1]) # reversed

print("hello" in a)
print("hello" not in a)

print(len(a))

#CASE CONVERDION METHODS-->
a.upper()
a.lower()
a.title()
a.capitalize()
a.swapcase()

#SEARCHING METHODS--->
text = "python prograaming"

print(text.find("hg"))

#rfind()
#index()
#rindex()

# VALIDATION METHODS--->
# isdigit()
# isalpha()
# isalnum()
# isspace()
# istitle()

print(text.replace("python","java"))

text.split()
text.split("o")

text1 = "python"
print(text1.ljust(10)) #add width
print(text1.rjust(10))
print(text1.center(10))

text.strip() #remove white strip
text.lstrip() #remove left white strip
text.rstrip() #remove right white strip

#STRING FORMATING--->
name = "alice"
age = 20

print(f"hello,{name}")
print("hello, {}" .format(name))

# PALINDROM CHECKER---->
def is_palindrom(str):
    str = str.upper()
    str = str.replace(" ","")
    if str == str[::-1]:
        print("palindrom")
    else:
        print("not palindrom")


is_palindrom("nitIn")

# HALF PYRAMID--->
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(i+1):
        print("*", end = " ")
    print()
    
# EXEPTION HANDLING--->
# an exeption handling is an error that happens while your programming is running

# Basic syntax-->
#try:
    """ code may couse error"""
#except:
    """code that runs if error occures"""

print("hello")

try:
    print(z)
except:
    print("error")

#else:
# finally:
# raise exeption("wrong")

#  FILE HANDLING--->
# open(filename, mode)

#  4 main modes
# 1.read r
# 2.append a
# 3.write w
# 4.creat x
# 
# after that we need to close the file also
# f = open("file_name") default mode is read r
# f.close()