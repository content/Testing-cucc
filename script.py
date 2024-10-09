import pygame

def calculateSum(a, b):
    return a + b

def calculateDifference(a, b):
    return a - b

def calculateProduct(a, b):
    return a * b

def calculateQuotient(a, b):
    return a / b

# Create a calculator project
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation: ")
if(operation == '+'):
    print(calculateSum(num1, num2))
elif(operation == '-'):
    print(calculateDifference(num1, num2))
elif(operation == '*'):
    print(calculateProduct(num1, num2))
elif(operation == '/'):
    print(calculateQuotient(num1, num2))