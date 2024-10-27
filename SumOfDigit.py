num = int(input("enter the number:"))
sum1 = 0
while num != 0:
    rem = int(num % 10)
    sum1 = int(sum1 + rem)
    num = int(num /10)
print("sum of digits:", sum1)