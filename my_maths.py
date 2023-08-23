


def calculate(operator, num1, num2):
	operator=input("Enter your operator:\n")
	if (operator == "add" or operator=="ADD"):
		print (num1 + num2)
	elif (operator == "subtract" or operator=="SUBTRACT"):
		print (num1 - num2)
	elif (operator == "multiply" or operator=="MULTIPLY"):
		print (num1 * num2)
	elif (operator == "divide" or operator=="DIVIDE"):
		print (num1 / num2)
print (calculate("",2,4))

	
