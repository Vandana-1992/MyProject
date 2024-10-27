#   length = int(len(string1))
#   print("length of string is:", length)
#    for i in range(0,length):
#        if string1[i] != string1[length-i-1]:
#            return 0
#        return 1
def palindrome(string1):
    orig = string1
    rev = string1[ : :-1]
    if orig == rev:
        return 1
    else:
        return 0

str1 = input("enter a string:")
res = palindrome(str1)
if res == 1:
    print("yes pallindrome")
else:
    print("Not a palindrome")