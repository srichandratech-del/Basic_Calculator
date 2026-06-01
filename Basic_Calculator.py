# Simple Calculator With Basic Functions

a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))
c = float(input("Enter Third Number: "))
Operator = input("Enter operation (add/sub/mul/div): ")

if  Operator == "Add" or Operator == "Addition" or Operator == "+" :
    print(a + b + c)
elif Operator == "Sub" or Operator == "Subtraction" or Operator == "-":
    print(a - b - c)
elif Operator == "Mul" or Operator == "Multipication" or Operator == "*":
    print(a * b * c)
elif Operator == "Div"or Operator == "Division" or Operator == "/":
    if b !=0:
        print(a / b / c)
    else:
        print("Syntax Error")
    
else:
    print("Invalid Operation")