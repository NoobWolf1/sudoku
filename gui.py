import pygame, sys
from pygame.locals import *

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


def main():
	global FPSClock, DisplaySurf, BasicFont, BasicFontSize
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
		for event in pygame.event.get():
			if event.type == QUIT :
				run = False 
				pygame.quit()
				sys.exit()

		pygame.display.update()
		FPSClock.tick(FPS)



if __name__ == '__main__':
	main()