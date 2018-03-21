age= 76

def start():
	number = input("guess my number")
	hello =int(number)
	checknumber(hello)

def checknumber(guessedNumber):
	if guessedNumber < age:
		print("your number is less than mine")
		tryagain()
		
	elif guessedNumber > age: 
		print ("your number is greater than mine")
		tryagain()
		
	else:
		print ("congratualations you won :)")
	

def tryagain():
	number = input("guess again")
	hello = int(number)
	checknumber(hello)

start()
