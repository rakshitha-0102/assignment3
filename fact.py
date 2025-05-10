num=int(input("Enter a number : "))
def factorial(num):
    fact = 1
    if (num == 0) or (num == 1):
        return 1
    else:
        for i in range(1,num+1):
            fact *= i
        return fact
result = factorial(num)
print("factorial of",num,"is :",result)