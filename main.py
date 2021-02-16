from functions import *

print("What do you want to do?")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

num1 = int((input("enter number1: ")))
num2 = int((input("enter number2: ")))


if choice == 1:
        addition(num1, num2)
        
elif choice == 1:
        subtraction(num1, num2)

elif choice == 1:
        multiplication(num1, num2)

elif choice == 1:
        division(num1, num2)



