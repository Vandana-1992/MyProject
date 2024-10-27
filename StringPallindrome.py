str1 = input("enter a string:")
rev = str1[: : -1]
if rev == str1:
    print("String is palindrome")
else:
    print("String is not palindrome")