# WRITE A FUNCTION THAT TAKES A SENTANCE AND RETURN IT WITH EVERY WORD CAPITLIZED
def capitlizes(str):
    words = str.split()
    result = []

    for word in words:
        result.append(word.capitalize())

    return(" ".join(result))

print(capitlizes("nitish is a boy"))

# WRITE A PROGRAM THAT CHEAKS WHETHER A GIVEN IS AN ANANGRAM OF ANOTHER STRING
strr = "silent"
str1 = "listen"

if len(strr) == len(str1):
    if sorted(strr) == sorted(str1):
        print("ANANGRAM")
    else:
        print("NOT ANANGRAM")

# COUNT THE FREQUENCY OF EACH CHARACTER IN A STRING. PRINT ONLT CHARACTER THAT APPEAR MORE THAN ONCE.
def frequency(strrr):
    result = ""
    for ch in strrr:
        count = 0
        for c in strrr:
            if ch == c:
                count += 1

        if count>1 and ch not in result:
            result += ch
    
    return(result)
print(frequency("pyython"))

# WRITE A PROGRAM TO PRINT A RIGHT ANGLED TRIANGLE OF NUMBERS.
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end = " ")
    print("")
 
# REMOVE ALL VOLWELS FROM A GIVEN STRING.
def remove_vowel(words):
    vowels = "aeiouAEIOU"
    result = ""

    for ch in words:
        if ch not in vowels:
            result += ch

    print(result)

remove_vowel("python is programming l")