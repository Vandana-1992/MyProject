num = int(input("Enter a number: "))
tmp = num
div = 0
for i in range(1, num):
    if num % i == 0:
        div = div + i

if tmp == div:
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")