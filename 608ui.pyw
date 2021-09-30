#!/usr/bin/python3
import random
import pygame as pg
from time import sleep
from tkinter import *
from tkinter import messagebox
X = 10
Y = 10
x = random.randint(0,X-1)
y = random.randint( 0,Y-1)
size = 500
Mess = ""
flag = False
logo = 50
bottom = 100

color1 = (132, 165, 184) #header
color2 = (66,104,124) #background
color3 = (179, 218, 241) #boards
def reset(DISPLAY):
	

	pg.display.set_caption("608")
	background=color2

		
	DISPLAY.fill(background)
	font = pg.font.Font(None, 50)
	textlogo = font.render("608", 1, color1)
	DISPLAY.blit(textlogo,(size//2-55,0))
	global Mess
	global x
	global y
	x = random.randint(0,X-1)
	y = random.randint( 0,Y-1)
	Mess = ""
	return DISPLAY
def render(DISPLAY):
	global Mess
	global x 
	global y 
	

	for j in range(0,X+1):
		for i in range(0,X+1):
			if (i == x and j == y ):
				message = "608"
			else: message = "609"
			font = pg.font.Font(None, 30)
			text = font.render(message, 1, color3)

			DISPLAY.blit(text,(((size/ X) * i ) + 5 ,((size/X) * j)+ 10+logo))
		

			DISPLAY.blit(text,(((size/ X) * i ) + 5 ,((size/X) * j)+ 10+logo))
		text2 = font.render(Mess, 1, color1)
		DISPLAY.blit(text2,(size//2,size+bottom//2+logo))

def main():
	pg.init()
	DISPLAY=pg.display.set_mode((size ,size+bottom+ logo),0,32)	
	reset(DISPLAY)
	render(DISPLAY)
	while True:
		for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
				if event.type == pg.MOUSEBUTTONUP:	
					onclick()
					render(DISPLAY)
					pg.display.update()
					global flag
				if flag:
					flag = False
					sleep (1)					
					reset(DISPLAY)
					render(DISPLAY)
				pg.display.update()
				

def onclick():
	xi,yi= pg.mouse.get_pos()
	i1 = int((xi-5)/size*X)
	i2 = int((yi-10-logo)/size*Y)
	if i1 == x and i2 == y:
		global Mess,flag
		Mess = "YEAH !!!! "
		flag = True
		
	
main()

