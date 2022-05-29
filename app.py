# Importing modules
from  helpers.addition import add
from helpers.division import div
from helpers.multiplication import multi
from helpers.subtraction import sub

print ("Welcome to Simple Calculator")
print ("Select from the Following:")
print ("1: Addition")
print ("2: Subtraction")
print ("3: Multiplication")
print  ("4: Division")

operation = input("Please enter your selection 1/2/3/4:")
try:
    result = int(operation)
except ValueError:
    print("Valid Input")
    exit()

num1 = int (input ("Enter your first number:"))
try:
    result = int(result)
except ValueError:
    print("Valid Input")
    exit()

num2 = int(input ("Enter your second number:"))
try:
    result = int(result)
except ValueError:
    print("Valid Input")
    exit()

if operation == "1":
    result= add(num1,num2)
    print( num1, "+", num2, "=" ,(result))
elif operation == "2":
    result = sub(num1,num2)
    print( num1, "-", num2, "=" ,(result))
elif operation == "3":
    result = multi(num1,num2)
    print( num1, "x", num2, "=" ,(result))
elif operation == "4":
    try:
        result = div(num1,num2)
        print( num1, "/", num2, "=" ,(result))
    except ZeroDivisionError:
        print(" Error, You tried dividing by 0")





    







# result = input ("Please enter your selection:")
# result = input ("Enter your first number:")
# result = input ("Enter your second number:")






# result = add(9,8)
# print(result)

# result = sub(25, 7)
# print(result)

# result = multi (5,9)
# print(result)

# result = div (24, 6)
# print(result)