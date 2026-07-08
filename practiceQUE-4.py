# CREATE A LIST OF 5 NUMBERS. PRINT THE LIST REVERSED WITHOUT USING REVERSE() OR REVERSED().
list = [1,2,3,4,5]
print(list[::-1])

sum = 0
for i in list:
    sum = i + sum
print(sum)

# GIVEN A DICTIONARY OF {COUNTRY: CAPITAL}, WRITE A FUNCTION THAT TAKES A COUNTRY NAMES AND RETURN ITS CAPITAL (OR NOT FOUND).
dictionary = {
    "india": "delhi",
    "Bihar": "Patna",
    "punjab": "Mohali",
}

def country(key):
    if key in dictionary:
        print(dictionary[key])
    else:
        print("NOT FOUND")

country("africa")

#CREATE A LIST OF STUDENTS MARKS REMOVE ALL STUDENTS WHO SCORED BELOW 40(USE LOOP-NOT LIST COMPREHINSION).
marks = [67,87,43,21,56]
for i in marks:
    if i<40:
        marks.remove(i)
print(marks)

#CONVERT A LIST OF WORDS INTO A DICTIONARY WHERE A KEY = WORDS, VALUE = LENGTH OF WORD.
listtt = ["abc", "apple", "banana", "orange"]

def dictionaryy(li):
    result = {}

    for word in li:
        count = 0

        for i in word:
            count += 1

        result[word] = count

    print(result)

dictionaryy(listtt)

# WRITE A PROGRAM TO COUNT HOW MANY TIMES EACH LETTER APPEARS IN A GIVEN STRING USING A DICTIONARY.
str = "Hello"
dic = {}

for ch in str:
    if ch in dic:
        dic[ch] += 1
    else:
        dic[ch] = 1

print(dic)