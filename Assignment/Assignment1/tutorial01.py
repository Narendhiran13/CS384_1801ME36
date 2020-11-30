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
		if isinstance(num2,int) or isinstance(num2,float):
			power = 1 
			for i in range(num2):

				if num2 == 0: 
					return 1
	
				power = power * num1
	
		else:
			return "Enter Valid Number"			
	else:
		return "Enter Valid Numbesr"			
	
	#DivisionLogic 
	return power
	
# Python 3 program to print GP.  geometric Progression
#You cant use the inbuilt python function. Write your own function
def printGP(a, r, n):
	gp=[]
	if isinstance(a,int) or isinstance(a,float):
		if isinstance(r,int) or isinstance(r,float):
			if isinstance(n,int):
				if n == 0: # r cannot be zero, but n can be zero
					for i in range(5): gp.append(a)
					
				for i in range(n):
					Var = a * power(r,i)
					gp.append(Var)
			else:
				return "Enter Valid Numbesr"
		else:
			return "Enter Valid Number"			
	else:
		return "Enter Valid Numbesr"			

	return gp 

# Python 3 program to print AP.  arithmetic Progression
#You cant use the inbuilt python function. Write your own function
def printAP(a, d, n): 
	ap=[] 
	if isinstance(a,int) or isinstance(a,float):
		if isinstance(d,int) or isinstance(d,float):
			if isinstance(n,int):
				if n <= 0:
					return "Enter Valid Value for 'n', postive  & non zero values!"
				for i in range(n):
					Var = a + i* d
					ap.append(Var)

			else:
				return "Enter Valid Numbesr"
		else:
			return "Enter Valid Number"			
	else:
		return "Enter Valid Numbesr"			

	return ap

# Python 3 program to print HP.   Harmonic Progression
#You cant use the inbuilt python function. Write your own function
def printHP(a, d, n): 
	hp=[]
	if isinstance(a,int) or isinstance(a,float):
		if isinstance(d,float) or isinstance(d,int):
			if isinstance(n,int):
				if n <= 0:
					return "Enter Valid Value for 'n', can be postive  & non zero values!"
				for i in range(0,n):
					f = a + d*i
					if f == 0:
						hp.clear()
						hp.append(0)
						return hp
					hp.append(round(1/(a+d*i),3))
			else:
				return "Enter Valid Number"	
		else:
			return "Enter Valid Number"			
	else:
		return "Enter Valid Number"			
	return hp


