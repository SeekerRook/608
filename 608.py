import random
for i in range (50):
	print("")
with open('logo.txt', 'r') as f:
    print(f.read())
print("by SeekerRook")
print ("\n\nFind th 608 among the 609")
print("\n\n At any point in the game press CTRL+C to Quit")
print ("\n\nAre you ready ?? (Press ENTER to Start)\n\n\n\n")
Choice = input()
while (True):
	try:
		X = 10
		Y = 10
		x = random.randint(0,X-1)
		y = random.randint( 0,Y-1)
		for i in range (50):
				print("")
		print ("   ", end = "")
		for j in range (X):
			print("x"+str(j+1), end = "   ")
		print ("")
		for i in range (X):
			print("y"+str(i+1),end = "")
			for j in range (Y):
				if (i == x and j == y ):
					print (" 608 ", end = "")
				else: print (" 609 ", end="")
			print ('\n')
		for i in range(4):
			print("")
		flag = True
		while flag:
			yi = input("x = ")
			if yi == "h":
				print (y+1, x+1)
				yi = int(input("x = "))
			else: yi = int(yi)
			xi = int(input("y = "))

			if (xi-1 == x and yi-1 == y):
				print("yeah")
				flag = False
			else : print (" oh no " )
			Choice = input("hit ENTER to continue or CTRL+C to Exit : ")
			for i in range (50):
				print("")
	except KeyboardInterrupt:
		print ("\n\nBye\n\n")
		exit() 