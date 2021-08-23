import random

X = 7
Y = 10
x = random.randint(0,X-1)
y = random.randint( 0,Y-1)
for i in range (15):
	print("")
for j in range (X):
	print(j+1,end = " ")
for i in range (Y):
	print(i+1)
	for j in range (X):
		if (i == x and j == y ):
			print (" 608 ", end = "")
		else: print (" 609 ", end="")
	print ('\n')
for i in range(4):
	print("")
xi = int(input())
yi = int(input())

if (xi-1 == x and yi-1 == y):
	print("yeah")
else : print (" oh no " )
