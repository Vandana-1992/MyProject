def EvenOdd(Number):
    if Number == 0:
        return 0
    elif Number == 1:
        return 1
    else:
        if (Number % 2 != 0):
            return 1
        else :
            return 0

Num = int(input("Enter a number: "))
result = EvenOdd(Num)
if result == 1:
    print("Odd")
else:
    print("Even")