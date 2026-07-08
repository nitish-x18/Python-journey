str = "I am a boy who lived in mohali for my education"
print(str.split())
print(str[3])
rev = ""
for ch in str:
    rev = ch + rev

print(rev)

s = "hello"

wave = ""
for i in range(len(rev)):
    if i % 2 == 0:
        wave += rev[i].upper()
    else:
        wave += rev[i].lower()
    
print(wave)