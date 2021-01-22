import random, pygame, sys
from pygame.locals import *

BOARDWIDTH = 6
BOARDHEIGHT = 6


FPS = 60
WIDTH = 640
HEIGHT = 480

pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((WIDTH, HEIGHT))

SPEEDDEMONSTRATION = 1
BOXSIZE = 40
GAPSIZE = 10

XMARGIN = int((WIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((HEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)


RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


CIRCLE = 'circle'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'


ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (CIRCLE, SQUARE, DIAMOND, LINES, OVAL)


def getRandomizedBoard():


    icons = []
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append((shape, color))
    random.shuffle(icons)



    numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2)
    icons = icons[:numIconsUsed] * 2
    random.shuffle(icons)



    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(icons[0])
            del icons[0]
        board.append(column)

    return board


def generateRevealedBoxesData(val):

    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)
    return revealedBoxes


def boxPos(boxx, boxy):


    bX = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    bY = boxy * (BOXSIZE + GAPSIZE) + YMARGIN

    return (bX, bY)


def getBoxAtPixel(x, y):


    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            boxRect = pygame.Rect(boxPos(boxx, boxy)[0], boxPos(boxx, boxy)[1], BOXSIZE, BOXSIZE)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)

    return (None, None)


def drawIcon(shape, color, boxx, boxy):


    if shape == CIRCLE:
        pygame.draw.circle(display, color,
                           (boxPos(boxx, boxy)[0] + int(BOXSIZE * 0.5), boxPos(boxx, boxy)[1] + int(BOXSIZE * 0.5)),
                           int(BOXSIZE * 0.5) - 5)

    elif shape == SQUARE:
        pygame.draw.rect(display, color, (
            boxPos(boxx, boxy)[0] + int(BOXSIZE * 0.25), boxPos(boxx, boxy)[1] + int(BOXSIZE * 0.25),
            BOXSIZE - int(BOXSIZE * 0.5), BOXSIZE - int(BOXSIZE * 0.5)))

    elif shape == DIAMOND:
        pygame.draw.polygon(display, color, (
            (boxPos(boxx, boxy)[0] + int(BOXSIZE * 0.5), boxPos(boxx, boxy)[1]),
            (boxPos(boxx, boxy)[0] + BOXSIZE - 1, boxPos(boxx, boxy)[1] + int(BOXSIZE * 0.5)),
            (boxPos(boxx, boxy)[0] + int(BOXSIZE * 0.5), boxPos(boxx, boxy)[1] + BOXSIZE - 1),
            (boxPos(boxx, boxy)[0], boxPos(boxx, boxy)[1] + int(BOXSIZE * 0.5))))

    elif shape == LINES:
        for i in range(0, BOXSIZE, 4):
            pygame.draw.line(display, color, (boxPos(boxx, boxy)[0], boxPos(boxx, boxy)[1] + i),
                             (boxPos(boxx, boxy)[0] + i, boxPos(boxx, boxy)[1]))
            pygame.draw.line(display, color, (boxPos(boxx, boxy)[0] + i, boxPos(boxx, boxy)[1] + BOXSIZE - 1),
                             (boxPos(boxx, boxy)[0] + BOXSIZE - 1, boxPos(boxx, boxy)[1] + i))

    elif shape == OVAL:
        pygame.draw.ellipse(display, color, (
            boxPos(boxx, boxy)[0], boxPos(boxx, boxy)[1] + int(BOXSIZE * 0.25), BOXSIZE, int(BOXSIZE * 0.5)))


def getShapeAndColor(board, boxx, boxy):


    return board[boxx][boxy][0], board[boxx][boxy][1]


def drawBoxCovers(board, boxes, coverage):


    for box in boxes:
        pygame.draw.rect(display, (0, 0, 0), (boxPos(box[0], box[1])[0], boxPos(box[0], box[1])[1], BOXSIZE, BOXSIZE))
        shape, color = getShapeAndColor(board, box[0], box[1])
        drawIcon(shape, color, box[0], box[1])

        if coverage > 0:
            pygame.draw.rect(display, (255, 255, 255),
                             (boxPos(box[0], box[1])[0], boxPos(box[0], box[1])[1], coverage, BOXSIZE))

    pygame.display.update()
    clock.tick(FPS)


def showBoxes(board, boxesToShow):


    for coverage in range(BOXSIZE, (-SPEEDDEMONSTRATION) - 1, - SPEEDDEMONSTRATION):
        drawBoxCovers(board, boxesToShow, coverage)
    for coverage in range(0, BOXSIZE + SPEEDDEMONSTRATION, SPEEDDEMONSTRATION):
        drawBoxCovers(board, boxesToShow, coverage)


def openBoxAnim(board, boxesToReveal):


    for coverage in range(BOXSIZE, (-SPEEDDEMONSTRATION) - 1, - SPEEDDEMONSTRATION):
        drawBoxCovers(board, boxesToReveal, coverage)


def closeBoxAnim(board, boxesToCover):


    for coverage in range(0, BOXSIZE + SPEEDDEMONSTRATION, SPEEDDEMONSTRATION):
        drawBoxCovers(board, boxesToCover, coverage)


def drawBoard(board, revealed):


    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            if not revealed[boxx][boxy]:


                pygame.draw.rect(display, (255, 255, 255),
                                 (boxPos(boxx, boxy)[0], boxPos(boxx, boxy)[1], BOXSIZE, BOXSIZE))

            else:



                shape, color = getShapeAndColor(board, boxx, boxy)
                drawIcon(shape, color, boxx, boxy)


def startGame(board):


    coveredBoxes = generateRevealedBoxesData(False)
    boxes = []
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            boxes.append((x, y))
    random.shuffle(boxes)
    drawBoard(board, coveredBoxes)
    showBoxes(board, boxes)


def hasWon(revealedBoxes):


    for i in revealedBoxes:
        if False in i:
            return False
    return True


mainBoard = getRandomizedBoard()
revealedBoxes = generateRevealedBoxesData(False)
firstSelection = None

display.fill((0, 0, 0))
startGame(mainBoard)
mousePosX = 0
mousePosY = 0

running = True
while running:
    mouseClicked = False
    display.fill((0, 0, 0))

    drawBoard(mainBoard, revealedBoxes)

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            running = False

        elif event.type == MOUSEMOTION:
            mousePosX, mousePosY = event.pos

        elif event.type == MOUSEBUTTONUP:
            mousePosX, mousePosY = event.pos
            mouseClicked = True

    boxx, boxy = getBoxAtPixel(mousePosX, mousePosY)
    if boxx != None and boxy != None:


        if not revealedBoxes[boxx][boxy] and mouseClicked:
            openBoxAnim(mainBoard, [(boxx, boxy)])
            revealedBoxes[boxx][boxy] = True



            if firstSelection == None:
                firstSelection = (boxx, boxy)

            else:

                icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
                icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)



                if icon1shape != icon2shape or icon1color != icon2color:

                    pygame.time.wait(500)
                    closeBoxAnim(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
                    revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                    revealedBoxes[boxx][boxy] = False

                elif hasWon(revealedBoxes):


                    mainBoard = getRandomizedBoard()
                    revealedBoxes = generateRevealedBoxesData(False)
                    drawBoard(mainBoard, revealedBoxes)
                    pygame.display.update()

                    pygame.time.wait(1000)
                    startGame(mainBoard)

                firstSelection = None

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
