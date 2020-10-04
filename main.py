print("welcome to simple python calculator")
v1 = float(input("first Value: "))
option = str(input("operation: "))
v2 = float(input("second Value: "))

elif option == "+":
	answer = v1+v2
	if answer-int(answer) == 0:
		answer = int(answer)
elif option == "-":
	answer = v1-v2
	if answer-int(answer) == 0:
		answer = int(answer)
elif option == "*":
	answer = v1*v2
	if answer-int(answer) == 0:
		answer = int(answer)
elif option == "/":
	answer = v1/v2
	if answer-int(answer) == 0:
		answer = int(answer)
else:
	answer = "the operation is just [+,-,*,/]"

print("answer:",answer)
