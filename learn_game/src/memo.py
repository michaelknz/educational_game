import random, pygame, sys
from pygame.locals import *

BOARDWIDTH = 6  # количество столбцов в игре
BOARDHEIGHT = 6  # количество строк в игре

# характеристики окна
FPS = 60
WIDTH = 640
HEIGHT = 480

pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((WIDTH, HEIGHT))

SPEEDDEMONSTRATION = 1
BOXSIZE = 40  # размер карточек
GAPSIZE = 10  # отступы между карточками

XMARGIN = int((WIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((HEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

# радуга палитра
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

# возможные фигуры
CIRCLE = 'circle'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

# цвета и формы
ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (CIRCLE, SQUARE, DIAMOND, LINES, OVAL)


def getRandomizedBoard():
    # создание случайного набора возможных комбинаций форм и цветов

    icons = []
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append((shape, color))
    random.shuffle(icons)

    # создание нужного количества пар и перемешивание их

    numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2)
    icons = icons[:numIconsUsed] * 2
    random.shuffle(icons)

    # создание доски
    # при этом список иконок сокращаем

    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(icons[0])
            del icons[0]
        board.append(column)

    return board


def generateRevealedBoxesData(val):
    # cоздание списка еще скрытых карточек
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)
    return revealedBoxes


def boxPos(boxx, boxy):
    # преобразование координат доски в пиксельные координаты

    bX = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    bY = boxy * (BOXSIZE + GAPSIZE) + YMARGIN

    return (bX, bY)


def getBoxAtPixel(x, y):
    # проверка наличия карточки на месте крысы

    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            boxRect = pygame.Rect(boxPos(boxx, boxy)[0], boxPos(boxx, boxy)[1], BOXSIZE, BOXSIZE)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)

    return (None, None)


def drawIcon(shape, color, boxx, boxy):
    # отрисовываем фигурки

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
    # получаем форму board[boxx][boxy][0]
    # получаем цвет board[boxx][boxy][1]

    return board[boxx][boxy][0], board[boxx][boxy][1]


def drawBoxCovers(board, boxes, coverage):
    # список карточек для отрисовки
    # отражает закрашенные и не закрашенные

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
    # показывает карточки перед игрой

    for coverage in range(BOXSIZE, (-SPEEDDEMONSTRATION) - 1, - SPEEDDEMONSTRATION):
        drawBoxCovers(board, boxesToShow, coverage)
    for coverage in range(0, BOXSIZE + SPEEDDEMONSTRATION, SPEEDDEMONSTRATION):
        drawBoxCovers(board, boxesToShow, coverage)


def openBoxAnim(board, boxesToReveal):
    # открытие карточки

    for coverage in range(BOXSIZE, (-SPEEDDEMONSTRATION) - 1, - SPEEDDEMONSTRATION):
        drawBoxCovers(board, boxesToReveal, coverage)


def closeBoxAnim(board, boxesToCover):
    # закрытие карточки

    for coverage in range(0, BOXSIZE + SPEEDDEMONSTRATION, SPEEDDEMONSTRATION):
        drawBoxCovers(board, boxesToCover, coverage)


def drawBoard(board, revealed):
    # отрисовка доски и карточек в обоих состояниях

    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            if not revealed[boxx][boxy]:
                # отрисовка закрытой карточки

                pygame.draw.rect(display, (255, 255, 255),
                                 (boxPos(boxx, boxy)[0], boxPos(boxx, boxy)[1], BOXSIZE, BOXSIZE))

            else:

                # отрисовка открытой карточки

                shape, color = getShapeAndColor(board, boxx, boxy)
                drawIcon(shape, color, boxx, boxy)


def startGame(board):
    # первоначальная отрисовка всего

    coveredBoxes = generateRevealedBoxesData(False)
    boxes = []
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            boxes.append((x, y))
    random.shuffle(boxes)
    drawBoard(board, coveredBoxes)
    showBoxes(board, boxes)


def hasWon(revealedBoxes):
    # проверка на выигрыш

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
        # получение клика по карточке и его обработка

        # если это закрытая карточка

        if not revealedBoxes[boxx][boxy] and mouseClicked:
            openBoxAnim(mainBoard, [(boxx, boxy)])
            revealedBoxes[boxx][boxy] = True

            # выбор первой карты

            if firstSelection == None:
                firstSelection = (boxx, boxy)

            else:

                icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
                icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)

                # если не совпадают

                if icon1shape != icon2shape or icon1color != icon2color:

                    pygame.time.wait(500)
                    closeBoxAnim(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
                    revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                    revealedBoxes[boxx][boxy] = False

                elif hasWon(revealedBoxes):
                    # сброс всего при выигрыше

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
