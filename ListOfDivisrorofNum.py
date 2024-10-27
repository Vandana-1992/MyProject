lst = []
num = int(input("Enter a number:"))
if (num == 0) | (num == 1):
    print("Invalid Operation")
    exit()
else:
    for i in range(1, num +1):
        if num % i == 0:
            lst.append(i)
    print("Divisor of given number :")
    print(lst)
