import random
import pygame as pg
X = 10
Y = 10
x = random.randint(0,X-1)
y = random.randint( 0,Y-1)
size = 500
def main():
	pg.init()

	DISPLAY=pg.display.set_mode((size,size),0,32)
	pg.display.set_caption("608")
	background=(200,200,250)
    

	DISPLAY.fill(background)
	for j in range(0,X+1):
		for i in range(0,X+1):
			if (i == x and j == y ):
				message = "608"
			else: message = "609"
			font = pg.font.Font(None, 30)
			text = font.render(message, 1, (0, 0, 50))

			DISPLAY.blit(text,(((size/ X) * i ) + 5 ,((size/X) * j)+ 10))
	while True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
    			
			pg.display.update()

def onclick():
	x,y = pg.mouse.get_pos()
	i1 = (x-5)/size*X
	i  
main()

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
