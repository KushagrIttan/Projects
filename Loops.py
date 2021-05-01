import sys
num1 = float(input("Enter base : "))
op = input("Enter operator: ")
num2 = float(input("Enter height : "))
num3 = (0.5)

if op == "*":
    print(num1 * num2 * num3)
else:
    print("Invalid Operator: ")

print ("Press Enter key to exit")
input()
sys.exit()