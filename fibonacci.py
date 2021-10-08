#Tis is the  Function for nth Fibonacci number

def Fibonacci(n):
	if n<0:
		print("Incorrect input")
	# 1st Fibonacci number is 0
	elif n==0:
		return 0
	# 2nd Fibonacci number is 1
	elif n==1:
		return 1
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)
#here we  write our  main program

print(Fibonacci(9))

