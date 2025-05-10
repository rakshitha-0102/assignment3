import math

number = int(input("Enter a number: "))

def calculate_math_operations(number):
    sqrt_num = math.sqrt(number)
    print("square root of",number,"is : ",sqrt_num)
    log_num = math.log(number)
    print("Logarithm :", log_num)
    sine_num = math.sin(number)
    print("Sine:",sine_num)
calculate_math_operations(number)



