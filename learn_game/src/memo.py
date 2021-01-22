import random, pygame, sys
from pygame.locals import *


class memo_game:
    def __init__(self, screen):
        self.BOARDWIDTH = 6  # количество столбцов в игре
        self.BOARDHEIGHT = 6  # количество строк в игре

        self.screen = screen

        self.SPEEDDEMONSTRATION = 1
        self.BOXSIZE = 40  # размер карточек
        self.GAPSIZE = 10  # отступы между карточками

        self.XMARGIN = int((WIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
        self.YMARGIN = int((HEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

        # радуга палитра
        self.RED = (255, 0, 0)
        self.ORANGE = (255, 128, 0)
        self.YELLOW = (255, 255, 0)
        self.GREEN = (0, 255, 0)
        self.CYAN = (0, 255, 255)
        self.BLUE = (0, 0, 255)
        self.PURPLE = (255, 0, 255)
        self.GRAY = (100, 100, 100)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        # возможные фигуры
        self.CIRCLE = 'circle'
        self.SQUARE = 'square'
        self.DIAMOND = 'diamond'
        self.LINES = 'lines'
        self.OVAL = 'oval'

        # цвета и формы
        self.ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
        self.ALLSHAPES = (CIRCLE, SQUARE, DIAMOND, LINES, OVAL)

    def getRandomizedBoard(self):
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

    def generateRevealedBoxesData(self, val):
        # cоздание списка еще скрытых карточек
        revealedBoxes = []
        for i in range(BOARDWIDTH):
            revealedBoxes.append([val] * BOARDHEIGHT)
        return revealedBoxes

    def boxPos(self,boxx, boxy):
        # преобразование координат доски в пиксельные координаты

        bX = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
        bY = boxy * (BOXSIZE + GAPSIZE) + YMARGIN

        return (bX, bY)

    def getBoxAtPixel(self, x, y):
        # проверка наличия карточки на месте крысы

        for boxx in range(BOARDWIDTH):
            for boxy in range(BOARDHEIGHT):
                boxRect = pygame.Rect(boxPos(boxx, boxy)[0], boxPos(boxx, boxy)[1], BOXSIZE, BOXSIZE)
                if boxRect.collidepoint(x, y):
                    return (boxx, boxy)

        return (None, None)

    def drawIcon(self, shape, color, boxx, boxy):
        # отрисовываем фигурки

        if shape == CIRCLE:
            pygame.draw.circle(screen, color,
                               (boxPos(boxx, boxy)[0] + int(BOXSIZE * 0.5), boxPos(boxx, boxy)[1] + int(BOXSIZE * 0.5)),
                               int(BOXSIZE * 0.5) - 5)

        elif shape == SQUARE:
            pygame.draw.rect(screen, color, (
                boxPos(boxx, boxy)[0] + int(BOXSIZE * 0.25), boxPos(boxx, boxy)[1] + int(BOXSIZE * 0.25),
                BOXSIZE - int(BOXSIZE * 0.5), BOXSIZE - int(BOXSIZE * 0.5)))

        elif shape == DIAMOND:
            pygame.draw.polygon(screen, color, (
                (boxPos(boxx, boxy)[0] + int(BOXSIZE * 0.5), boxPos(boxx, boxy)[1]),
                (boxPos(boxx, boxy)[0] + BOXSIZE - 1, boxPos(boxx, boxy)[1] + int(BOXSIZE * 0.5)),
                (boxPos(boxx, boxy)[0] + int(BOXSIZE * 0.5), boxPos(boxx, boxy)[1] + BOXSIZE - 1),
                (boxPos(boxx, boxy)[0], boxPos(boxx, boxy)[1] + int(BOXSIZE * 0.5))))

        elif shape == LINES:
            for i in range(0, BOXSIZE, 4):
                pygame.draw.line(screen, color, (boxPos(boxx, boxy)[0], boxPos(boxx, boxy)[1] + i),
                                 (boxPos(boxx, boxy)[0] + i, boxPos(boxx, boxy)[1]))
                pygame.draw.line(screen, color, (boxPos(boxx, boxy)[0] + i, boxPos(boxx, boxy)[1] + BOXSIZE - 1),
                                 (boxPos(boxx, boxy)[0] + BOXSIZE - 1, boxPos(boxx, boxy)[1] + i))

        elif shape == OVAL:
            pygame.draw.ellipse(screen, color, (
                boxPos(boxx, boxy)[0], boxPos(boxx, boxy)[1] + int(BOXSIZE * 0.25), BOXSIZE, int(BOXSIZE * 0.5)))

    def getShapeAndColor(self, board, boxx, boxy):
        # получаем форму board[boxx][boxy][0]
        # получаем цвет board[boxx][boxy][1]

        return board[boxx][boxy][0], board[boxx][boxy][1]

    def drawBoxCovers(self, board, boxes, coverage):
        # список карточек для отрисовки
        # отражает закрашенные и не закрашенные

        for box in boxes:
            pygame.draw.rect(screen, (0, 0, 0),
                             (boxPos(box[0], box[1])[0], boxPos(box[0], box[1])[1], BOXSIZE, BOXSIZE))
            shape, color = getShapeAndColor(board, box[0], box[1])
            drawIcon(shape, color, box[0], box[1])

            if coverage > 0:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (boxPos(box[0], box[1])[0], boxPos(box[0], box[1])[1], coverage, BOXSIZE))

        pygame.screen.update()
        clock.tick(FPS)

    def showBoxes(self, board, boxesToShow):
        # показывает карточки перед игрой

        for coverage in range(BOXSIZE, (-SPEEDDEMONSTRATION) - 1, - SPEEDDEMONSTRATION):
            drawBoxCovers(board, boxesToShow, coverage)
        for coverage in range(0, BOXSIZE + SPEEDDEMONSTRATION, SPEEDDEMONSTRATION):
            drawBoxCovers(board, boxesToShow, coverage)

    def openBoxAnim(self, board, boxesToReveal):
        # открытие карточки

        for coverage in range(BOXSIZE, (-SPEEDDEMONSTRATION) - 1, - SPEEDDEMONSTRATION):
            drawBoxCovers(board, boxesToReveal, coverage)

    def closeBoxAnim(self, board, boxesToCover):
        # закрытие карточки

        for coverage in range(0, BOXSIZE + SPEEDDEMONSTRATION, SPEEDDEMONSTRATION):
            drawBoxCovers(board, boxesToCover, coverage)

    def drawBoard(self, board, revealed):
        # отрисовка доски и карточек в обоих состояниях

        for boxx in range(BOARDWIDTH):
            for boxy in range(BOARDHEIGHT):
                if not revealed[boxx][boxy]:
                    # отрисовка закрытой карточки

                    pygame.draw.rect(screen, (255, 255, 255),
                                     (boxPos(boxx, boxy)[0], boxPos(boxx, boxy)[1], BOXSIZE, BOXSIZE))

                else:

                    # отрисовка открытой карточки

                    shape, color = getShapeAndColor(board, boxx, boxy)
                    drawIcon(shape, color, boxx, boxy)

    def startGame(self, board):
        # первоначальная отрисовка всего

        coveredBoxes = generateRevealedBoxesData(False)
        boxes = []
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                boxes.append((x, y))
        random.shuffle(boxes)
        drawBoard(board, coveredBoxes)
        showBoxes(board, boxes)

    def hasWon(self, revealedBoxes):
        # проверка на выигрыш

        for i in revealedBoxes:
            if False in i:
                return False
        return True

    def update(self):
        mainBoard = getRandomizedBoard()
        revealedBoxes = generateRevealedBoxesData(False)
        firstSelection = None

        screen.fill((0, 0, 0))
        startGame(mainBoard)
        mousePosX = 0
        mousePosY = 0

        running = True
        while running:
            mouseClicked = False
            screen.fill((0, 0, 0))

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
                            pygame.screen.update()

                            pygame.time.wait(1000)
                            startGame(mainBoard)

                        firstSelection = None

            pygame.screen.update()
            clock.tick(FPS)
