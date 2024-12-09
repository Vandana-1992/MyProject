lis1 = []
lis2 = []
str1 = "Hi helllo 5 to 6 times"
for cont in str1.split():
    if cont.isdigit():
        lis1.append(cont)
print(lis1)
for word in str1.split():
    if word.isalpha():
        lis2.append(word)
print(lis2)
x = re.findall("\s", str1)
print("Space:", len(x))