#cheack the number is prime or not--->
def is_prime(x):
    if (x <= 1):
        print("Not Prime Number")
    
    else:
        for i in range(2,x):
            if x % i == 0:
                print("Not Prime Number")
                return
        print("Prime Number")

is_prime(1)

#Write a function to find maximum value in the list without using max function--->
def is_max(items):
    maximum = items[0]
    for i in items:
        if i>maximum:
            maximum = i
    print(maximum)

numbers = [1,2,4,3,7,4]
is_max(numbers)  

#write a function celcius to fahrenheit--->
def cal_to_for(c):
    print((9/5)*c+32)

cal_to_for(0)
cal_to_for(100)
cal_to_for(37)

#write a function count vowels that return the numbers the number of vowels in the given string--->
def count_vowel(words):
    count = 0
    vowels = "aeiouAEIOU"

    for ch in words:
        if ch in vowels:
            count += 1

    print(count)

strr = "chandigharh"
count_vowel(strr)

#write a function total number that returns the sum of however many numbers are passed in--->
def total(*numbers):
    total = 0

    for num in numbers:
        total += num
    return total
print(total(1,2,3,4,5))
print(total(1,2,3))
print(total())

#write a function print profile that prints each key value pair it recievess one per line--->
def print_profile(**details):
    for key, value in details.items():
        print(key ," : ", value)
print_profile(name="Munna", age=20, city="Bihar")