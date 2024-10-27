num = int(input("Enter a number:"))
orig = num
sum1 = 0
while num > 0:
    rem = int(num % 10)
    sum1 = int(sum1 +(rem * rem * rem ))
    num = int(num/10)
if orig == sum1:
    print("The number is Armstrong")
else:
    print("The number is not Armstrong")

