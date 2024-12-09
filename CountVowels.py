vow = ["a", "e", "i", "o", "u"]
count = 0
word = input("enter the word:")
for character in word:
    if character in vow:
        count = count + 1
print("count:", count)