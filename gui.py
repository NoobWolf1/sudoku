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
b = list()

for i in range(0,9):
	a = []
	for j in range(0,9):
		if board[i][j] == 0:
			a.append(0)
		else :
			a.append(1)
	b.append(a)

print(b)
print(len(b))


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
Green = (0,255,0)
Red = (255,0,0)
def populateCells(board):
	i,j = 0,0
	for y in range (0,WindowHeight,CellSize):
		i = 0
		for x in range (0, WindowWidth,CellSize):

			if b[j][i] != 0 and board[j][i] != 0 :
				cellSurf = BasicFont.render('%s' %(board[j][i]) , True , Black )
				cellRect = cellSurf.get_rect()
				cellRect.topleft = (x+CellSize/3,y+CellSize/3)
				DisplaySurf.blit(cellSurf, cellRect)

			elif b[j][i] == 0 and board[j][i] != 0:
				cellSurf = BasicFont.render('%s' %(board[j][i]) , True , LightGrey )
				cellRect = cellSurf.get_rect()
				cellRect.topleft = (x+CellSize/3,y+CellSize/3)
				DisplaySurf.blit(cellSurf, cellRect)

			else:
				cellSurf = BasicFont.render('%s' %('_') , True , White )
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

	#base line
	pygame.draw.line(DisplaySurf,Black,(0,WindowHeight),(WindowWidth,WindowHeight))




def validSelection(mousex,mousey):
	if mousey <= WindowHeight:
		xnumber = (mousex - (mousex % CellSize)) // CellSize
		ynumber = (mousey - (mousey % CellSize)) // CellSize
		if b[ynumber][xnumber] == 0 :
			return True


def selectBox(mousex,mousey):
	xTopLeft = mousex -  (mousex % CellSize)
	yTopLeft = mousey -  (mousey % CellSize)

	xnumber =  xTopLeft // CellSize
	ynumber =  yTopLeft // CellSize


	if b[ynumber][xnumber] == 0 and mouseClicked is True   :
		pygame.draw.rect(DisplaySurf, Blue, (xTopLeft,yTopLeft,CellSize,CellSize), 3 )




def deselectBox():
	DisplaySurf.fill(White)
	drawGrid()
	populateCells(board)

def scribe_into(mousex,mousey,key,selectCellValue):
	x = mousex - (mousex % CellSize)
	y = mousey - (mousey % CellSize)
	xnumber = x // CellSize
	ynumber = y // CellSize

	if key == 0 :
		deleteCellValue(xnumber,ynumber)

	else:
		cellSurf = BasicFont.render('%s' %(key) , True , LightGrey )
		cellRect = cellSurf.get_rect()
		cellRect.topleft = (x+CellSize/3,y+CellSize/3)
		DisplaySurf.blit(cellSurf, cellRect)

	if selectCellValue and valid(board,key,(ynumber,xnumber)):
		print('naach')	
		updateBoard(key,mousex,mousey)

def deleteCellValue(xnumber,ynumber):
	board[ynumber][xnumber] = 0
	DisplaySurf.fill(White)
	drawGrid()
	populateCells(board)


def updateBoard(key,mousex,mousey):
	x = mousex - (mousex % CellSize)
	y = mousey - (mousey % CellSize)
	xnumber = x // CellSize
	ynumber = y // CellSize

	DisplaySurf.fill(White)
	drawGrid()
	populateCells(board)
	pygame.display.update()

	board[ynumber][xnumber] = key

	for i in range(len(board)):
		for j in range(len(board[i])):
			if b[j][i] == 0:
				if board[j][i] != 0:
					cellSurf = BasicFont.render('%s' %(key) , True , LightGrey )
					cellRect = cellSurf.get_rect()
					cellRect.topleft = (x+CellSize/3,y+CellSize/3)
					DisplaySurf.blit(cellSurf, cellRect)

def addClock(sec):

	#pygame.time.delay(300)

	mins = sec // 60
	sec = sec % 60
	hours = mins // 60
	mins = mins % 60
	timer = str()

	if mins < 10 and sec < 10 :
		timer = '0'+str(mins)+':'+'0'+str(sec)
	elif mins < 10 and sec >= 10 :
		timer = '0'+str(mins)+':'+str(sec)
	else:
		timer = str(mins)+':'+str(sec)

	print(timer)


	cellSurf = BasicFont.render('%s' %(timer) , True , Red )
	cellRect = cellSurf.get_rect()
	cellRect.topleft = (350+CellSize/3,450+CellSize/3)
	DisplaySurf.blit(cellSurf, cellRect)

	#pygame.time.delay(300)

	#DisplaySurf.fill(White)
	#drawGrid()
	#populateCells(board)

	
	






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

	#for timer
	start_ticks = pygame.time.get_ticks()   #starter tick


	DisplaySurf = pygame.display.set_mode((WindowWidth,WindowHeight+CellSize))
	pygame.display.set_caption('Sudoku')
	BasicFontSize = 30
	BasicFont = pygame.font.SysFont('Arial', BasicFontSize)

	DisplaySurf.fill(White)
	drawGrid()
	populateCells(board)

 
	run = True
	while run:

		seconds = (pygame.time.get_ticks() - start_ticks) // 1000
		
		addClock(seconds)

		
		for event in pygame.event.get():
			if event.type == QUIT :
				run = False 
				pygame.quit()
				sys.exit()

			#the movement of mouse
			if event.type == MOUSEMOTION:
				mousex,mousey = event.pos 
			if event.type == MOUSEBUTTONUP:
				mousexClick,mouseyClick = event.pos
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
						key = 0
					if event.key == pygame.K_RETURN:
						selectCellValue = True
		
			print(key,selectCellValue)
		
		if mouseClicked == True:
			clickCount += 1
			if validSelection(mousex,mousey) and clickCount%2 == 1:
				selectBox(mousex, mousey)
			else:
				deselectBox()


		if validSelection(mousex,mousey) and key is not None and clickCount %2 == 1:
			print('im here')
			scribe_into(mousexClick,mouseyClick,key,selectCellValue)


		#deleting clause
		if validSelection(mousex,mousey) and key == 0 and clickCount %2 == 1:
			clickCount += 1


		#reset clause
		if clickCount % 2 == 0:
			selectCellValue = False
			key = None

		mouseClicked = False
		#selectCellValue = False
		#key = None

		pygame.display.update()
		FPSClock.tick(FPS)



if __name__ == '__main__':
	main()