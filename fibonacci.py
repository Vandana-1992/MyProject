size1 = int(input("Enter the range you would like to have:"))
num1 = 0
num2 = 1
if size1 == 0:
    print("invalid")
elif size1 == 1:
    print(num1)
else:
    print(num1)
    print(num2)
    for i in range(2, size1):
        res = int(num1 + num2)
        print(res)
        num1 = num2
        num2 = res