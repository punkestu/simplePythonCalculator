print("welcome to simple python calculator")
v1 = float(input("first Value: "))
option = str(input("operation: "))
v2 = float(input("second Value: "))

if option == "+":
	print("answer:",v1+v2)
if option == "-":
	print("answer:",v1-v2)
if option == "*":
	print("answer:",v1*v2)
if option == "/":
	print("answer:",v1/v2)