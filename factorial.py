def fact_fun(num1):
    fact = 1
    for i in range(1, (num1+1)):
        fact = int((fact * i))
    return fact

num = int(input("Enter a number you would like to know the factorial:"))
res = fact_fun(num)
print("factorial of", num, "is:", res)
#fact = factorial(num) # builtin function
#print("The factorial of", num, "is", fact)



