import pygame, sys
from pygame.locals import *
from backtrackingAlgo import solve, valid

board = [
	[7,8,0,4,0,0,1,2,0],
	[6,0,0,0,7,5,0,0,9],
	[0,0,0,6,0,1,0,7,8],
	[0,0,7,0,4,0,2,6,0],
	[0,0,1,0,5,0,9,3,0],
	[9,0,4,0,6,0,0,0,5],
	[0,7,0,3,0,0,0,1,2],
	[1,2,0,0,0,7,4,0,0],
	[0,4,9,2,0,6,0,0,7]

]

#frame dimensions
WindowWidth = 270
WindowHeight = 270
FPS = 10

#grid dimensions
WindowMultiplier = 5
WindowSize = 90
WindowWidth = WindowMultiplier * WindowSize
WindowHeight = WindowMultiplier * WindowSize

SquareSize = (WindowSize * WindowMultiplier) // 3
CellSize = SquareSize // 3



#Colours
White = (255,255,255)
Black = (0,0,0)
LightGrey = (200,200,200)
Blue = (0,0,255)

def populateCells():
	i,j = 0,0
	for y in range(0,WindowHeight,CellSize):
		i = 0
		for x in range(0, WindowWidth, CellSize):

			if board[j][i] != 0:
				cellSurf = BasicFont.render('%s' %(board[j][i]) , True , Black )
				cellRect = cellSurf.get_rect()
				cellRect.topleft = (x+CellSize/3,y+CellSize/3)
				DisplaySurf.blit(cellSurf, cellRect)

			else:
				cellSurf = BasicFont.render('%s' %('_') , True , Black )
				cellRect = cellSurf.get_rect()
				cellRect.topleft = (x+CellSize/3,y+CellSize/3)
				DisplaySurf.blit(cellSurf, cellRect)

			i += 1
		j += 1


def drawGrid():
	# Draw minor lines

	#draw vertical lines
	for x in range(0, WindowWidth, CellSize):
		pygame.draw.line(DisplaySurf, LightGrey,(x,0), (x, WindowHeight))
	#draw horizontal lines
	for y in range(0, WindowHeight, CellSize):
		pygame.draw.line(DisplaySurf, LightGrey, (0,y), (WindowWidth, y))

	#Draw Major Lines

	#draw vertical lines
	for x in range(0,WindowWidth, SquareSize):
		pygame.draw.line(DisplaySurf,Black,(x,0),(x,WindowHeight))

	#draw horizontal lines
	for y in range (0,WindowHeight,SquareSize):
		pygame.draw.line(DisplaySurf,Black,(0,y),(WindowWidth,y))


	populateCells()

def validSelection(mousex,mousey):
	xnumber = (mousex - (mousex % CellSize)) // CellSize
	ynumber = (mousey - (mousey % CellSize)) // CellSize
	if board[ynumber][xnumber] == 0 :
		return True

def selectBox(mousex,mousey):
	xTopLeft = mousex -  (mousex % CellSize)
	yTopLeft = mousey -  (mousey % CellSize)

	xnumber =  xTopLeft // CellSize
	ynumber =  yTopLeft // CellSize


	if board[ynumber][xnumber] == 0 and mouseClicked is True   :
		pygame.draw.rect(DisplaySurf, Blue, (xTopLeft,yTopLeft,CellSize,CellSize), 3 )
		#checkIfKeyPressed()




def deselectBox(mousex,mousey):
	DisplaySurf.fill(White)
	drawGrid()

def scribe_into(mousex,mousey,key):
	x = mousex - (mousex % CellSize)
	y = mousey - (mousey % CellSize)
	xnumber = x // CellSize
	ynumber = y // CellSize


	if valid(board, key,(ynumber,xnumber)):
		cellSurf = BasicFont.render('%s' %(key) , True , LightGrey )
		cellRect = cellSurf.get_rect()
		cellRect.topleft = (x+CellSize/3,y+CellSize/3)
		DisplaySurf.blit(cellSurf, cellRect)

		



#write a code to scribe into the board
#include functions from backtrackingAlgo.py


def main():
	global FPSClock, DisplaySurf, BasicFont, BasicFontSize, mouseClicked,clickCount
	clickCount = 0

	#selectCellValue = False
	selectCellValue = False
	key = None

	mouseClicked = False
	mousex = 0
	mousey = 0
	pygame.init()
	FPSClock = pygame.time.Clock()


	DisplaySurf = pygame.display.set_mode((WindowWidth,WindowHeight))
	pygame.display.set_caption('Sudoku')
	BasicFontSize = 30
	BasicFont = pygame.font.SysFont('Arial', BasicFontSize)

	DisplaySurf.fill(White)
	drawGrid()
	
	run = True
	while run:

		#checkMouseMotion()

		for event in pygame.event.get():
			if event.type == QUIT :
				run = False 
				pygame.quit()
				sys.exit()
			#the movement of mouse
			if event.type == MOUSEMOTION:
				mousex,mousey = event.pos 
			if event.type == MOUSEBUTTONUP:
				mousex,mousey = event.pos
				mouseClicked = True


			if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_1:
						key = 1
					if event.key == pygame.K_2:
						key = 2
					if event.key == pygame.K_3:
						key = 3
					if event.key == pygame.K_4:
						key = 4
					if event.key == pygame.K_5:
						key = 5
					if event.key == pygame.K_6:
						key = 6
					if event.key == pygame.K_7:
						key = 7
					if event.key == pygame.K_8:
						key = 8
					if event.key == pygame.K_9:
						key = 9
					if event.key == pygame.K_DELETE or event.key ==  pygame.K_BACKSPACE:
							#board.clear()
						key = None
					if event.key == pygame.K_RETURN:
						selectCellValue = True
			print(key,selectCellValue)

		

			
		

		
		if mouseClicked == True:
			clickCount += 1
			if validSelection(mousex,mousey) and clickCount%2 == 1:
				selectBox(mousex, mousey)
			else:
				deselectBox(mousex,mousey)


		if validSelection(mousex,mousey) and key is not None and clickCount %2 == 1:
			print('im here')
			scribe_into(mousex,mousey,key)



		mouseClicked = False
		selectCellValue = False
		key = None
		#selectCellValue = False

	

		pygame.display.update()
		FPSClock.tick(FPS)



if __name__ == '__main__':
	main()