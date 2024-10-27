num = int(input("enter a number:"))
tmp = num
sum1 = 0
while num > 0:
    rem = int(num % 10)
    sum1 = int((sum1 * 10) + rem)
    num = int(num /10)
if tmp == sum1:
    print("pallindrome")
else:
    print("not pallindrome")
