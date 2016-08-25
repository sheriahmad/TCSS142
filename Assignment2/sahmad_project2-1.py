### Sheheryar Ahmad
### TCSS 142
### Project 2
##



#setting up chars 
chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def input_number():
	while (True):
		num = input("Enter Napier's number: ")
		if (num.isalpha()):
			break
		print('Something is wrong. Try again.')
	return num

#defining math operator

def input_operator():
	while (True):
		op = input("Enter the desired arithmetic operation: ")
		if (op in ["+","-","*","/"]):
			break
		print('Something is wrong. Try again.')
	return op 


def napien_string_to_number(string):
	result = 0
	for char in string:
		result += 2**(chars.index(char))
	return result

#adding math logic
def apply_operator(n1, n2, op):
	if op == '+':
		return n1 + n2
	elif op == '-':
		return n1 - n2
	elif op == '*':
		return n1 * n2
	elif op == '/':
		return n1 // n2

def number_to_napien_string(number):
	result = ""
	if number == 0:
		result += "\"\""
	if number < 0:
		result += "-"
		number *= -1
	i = 0
	while (number > 0):
		pair = divmod(number, 2)
		number = pair[0]
		if pair[1] == 1:
			result += chars[i]
		i += 1
	return result

while (True):
	napien_num1 = input_number()
	num1 = napien_string_to_number(napien_num1)
	print("The first number is:", num1)
	napien_num2 = input_number()
	num2 = napien_string_to_number(napien_num2)
	print("The second number is:", num2)
	op = input_operator()
	result = apply_operator(num1,num2,op)
	print("The result is", result, number_to_napien_string(result))
	repeat = False
	while True:
		ask = input("Do you want to repeat the program? Enter y for yes, n for no: ")
		if ask == "y":
			repeat = True
			break
		elif ask == "n":
			break
	if repeat == False:
		break




#Other approches that didn't work

###alphabet = "abcdefghijklmnopqrstuvwxyz"
##
##def main():
##    askNum1 = input("Enter Napier's number: ")
##    askNum2 = input("Enter Napier's number again: ")
##    askSign = input("Enter the desired arithmetic operation(+,-,*,/): ") 
##    checkInput(askNum1, askNum2, askSign)
##    
##def checkInput(askNum1, askNum2, askSign): # check if the inputs satisfy the requirement
##    for ch in askNum1:
##        while not ch.isletter(): # anything that is not letter is invalid
##            print("Something is wrong, try again.")
##            
## #   for var in askNum2:
##        
##    for el in askSign:
##        while el != '+' or el != '-' or el != '*' or el != '/': # anything other than these 4 operators is invalid
##            print("Something is wrong, try again.")
##        
##
##    
##def calculateNapier(): # convert letter to decimal numeral
##    total = 0   # this is the counter for the sum of digits
##    for var in askNum1:
##        notation = ord(var) - ord('a')
##        number = 2 ** notation
##        total += number
##
##def operators(output1,input2,signInput):
##    sumTotal=0
##    sign = askSign
##    
##    if sign == "-":
##        sumTotal = askNum1 - askNum2
##    elif sign == "+":
##        sumTotal = askNum1 + askNum2
##    elif sign == "*":
##        sumTotal = askNum1 * askNum2
##    elif sign == "/":	
##        if askNum2 == 0:
##            print("Can't divide by O ")
##        else:
##            sumTotal = askNum1 / askNum2            
##    else:
##        print("This is not a valid operation")
##
##    return sumTotal
##
###def calculateBinary(): # convert the result of 2 numbers and the operator to binary
##    #use sumTotal and print in 2 styles: abcd and real numbers
##    
###def printingOut(): # print out the result in both notations
##
###def fixRepeat(): # make sure the letters are not repeat
##
##
##main()
##



##
##
##
##
##
##errorLoop = True
##while errorLoop:
##    
##    num1 = str(input("Enter Napier's number: "))
##    num2 = str(input("Enter second Napier's number: "))
##
##
##    if any( [ i >'z' or i<'a' for i in num1] and [i >'z' or i<'a' for i in num2]):
##        print("Something is wrong. Try again")
##
##
##
##    # Checks to make sure arithmetic operation is valid
##validOperation = False
##while not validOperation:
##        operation = input("Enter the desired arithmetic operation: ")
##        if operation == "+":
##                result = num1 + num2
##                validOperation = True
##        elif operation == "-":
##                result = num1 - num2
##                validOperation = True
##        elif operation == "*":
##                result = num1 * num2
##                validOperation = True
##        elif operation == "/" or operation == "%":
##                if num2 == 0:
## 
##
##        print(result)
##
