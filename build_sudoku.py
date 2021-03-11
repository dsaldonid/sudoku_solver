# Author: Diego Saldonid
# Date: 3/10/2021
# Description: Build sodoku board 

import requests
import sys, pygame as pg
import requests
from bs4 import BeautifulSoup
# from settings import *
# from buttonClass import *


#create number grid 
#to_do: have number_grid generate random puzzle
number_grid =[
	[1,2,3,4,5,6,7,8,9],
	[1,2,3,4,5,6,7,8,9],
	[1,2,3,4,5,6,7,8,9],
	[1,2,3,4,5,6,7,8,9],
	[1,2,3,4,5,6,7,8,9],
	[1,2,3,"",5,6,7,8,9],
	[1,2,3,4,5,6,7,8,9],
	[1,2,3,4,5,6,7,8,9],
	[1,2,3,4,5,6,7,8,9]
]

pg.init()
screen_size = 750,750
screen = pg.display.set_mode(screen_size)
font = pg.font.SysFont(None,80)

def make_background():
	#make our game background any color we want
	screen.fill(pg.Color("white"))

	#draw grid
	pg.draw.rect(screen,pg.Color("black"),pg.Rect(15,15,720,720), width=10)

	i = 1
	while (i*80) <720:
		line_width = 5 if i %3 >0 else 10
		#draw our rows and columns 
		pg.draw.line(screen,pg.Color("black"),pg.Vector2((i*80)+15,15),pg.Vector2((i*80)+15,735),line_width)
		pg.draw.line(screen,pg.Color("black"),pg.Vector2(15,(i*80)+15),pg.Vector2(735,(i*80)+15),line_width)
		i+=1


def draw_numbers():
	row = 0 
	offset = 35
	while row<9:
		col = 0
		while col < 9:
			output = number_grid[row][col]
			number_text = font.render(str(output),True,pg.Color('black'))
			screen.blit(number_text,pg.Vector2(col*80 +offset+4,row*80+offset-2))
			col +=1

		row+=1

def game_loop():
	#loop that will constant listen for any events in the game
	for event in pg.event.get():
		#if an event type specifies quitting the game, we exit the game
		if event.type == pg.QUIT: 
			sys.exit()

	#display our background 
	make_background()

	#add numbers on the board 
	draw_numbers()

	#updates display content 
	pg.display.flip()

while True:
	game_loop()