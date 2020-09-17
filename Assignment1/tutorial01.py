# Function to add two numbers 
def add(num1, num2): 
	addition = num1 + num2
	return addition

# Function to subtract two numbers 
def subtract(num1, num2): 
	subtraction = num1 - num2
	return subtraction

# Function to multiply two numbers 
def multiply(num1, num2):
	#Multiplication Logic 
	multiplication = num1 * num2
	return multiplication

# Function to divide two numbers 
def divide(num1, num2): 
	#DivisionLogic 
	division = num1 /num2
	return division
		
# Function to add power function
# You cant use the inbuilt python function x ** y . Write your own function
def power(num1, num2): #num1 ^ num2
	if isinstance(num1,int) or isinstance(num1,float):
		if isinstance(num2,float) or isinstance(num2,int):
			power = 1 
			for i in range(num2):

				if num2 == 0: 
					return 1 
	
				power = power * num1
	
		else:
			return "Enter Valid Number"			
	else:
		return "Enter Valid Number"			
	
	#DivisionLogic 
	return power
	
# Python 3 program to print GP.  geometric Progression
#You cant use the inbuilt python function. Write your own function
def printGP(a, r, n): 
	gp=[] 

	return gp 

# Python 3 program to print AP.  arithmetic Progression
#You cant use the inbuilt python function. Write your own function
def printAP(a, d, n): 
	ap=[] 
	
	return ap

# Python 3 program to print HP.   Harmonic Progression
#You cant use the inbuilt python function. Write your own function
def printHP(a, d, n): 
	hp=[]
			
	return hp


