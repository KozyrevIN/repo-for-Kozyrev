import pygame
from random import randint
from pygame.draw import *

RED = (255, 000, 000)
BLUE = (000, 000, 255)
GREEN = (000, 255, 000)
B_GREEN = (170, 222, 105)
L_GREEN = (112, 200, 55)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 000)
GRAY = (128, 128, 128)
BLACK = (000, 000, 000)
SKY = (185, 211, 238)
PURPLE = (229, 128, 255)


def leg(pos, size, reverse=False):
    if not reverse:
        ellipse(screen, WHITE, pygame.Rect(pos[0], pos[1], round(15 * size), round(40 * size)))
        ellipse(screen, WHITE, pygame.Rect(pos[0], pos[1] + round(33 * size), round(15 * size), round(40 * size)))
        ellipse(screen, WHITE, pygame.Rect(pos[0], pos[1] + round(68 * size), round(20 * size), round(11 * size)))
    else:
        ellipse(screen, WHITE, pygame.Rect(pos[0] - round(15 * size), pos[1], round(15 * size), round(40 * size)))
        ellipse(screen, WHITE, pygame.Rect(pos[0] - round(15 * size), pos[1] + round(33 * size), round(15 * size),
                                           round(40 * size)))
        ellipse(screen, WHITE, pygame.Rect(pos[0] - round(20 * size), pos[1] + round(68 * size), round(20 * size),
                                           round(11 * size)))


def draw_lama(pos, size, reverse=False):
    if not reverse:
        lama_right(pos, size)
    else:
        lama_left(pos, size)


def lama_right(pos, size):
    reverse = False
    pos[0] = round(pos[0] * size)
    pos[1] = round(pos[1] * size)
    ellipse(screen, WHITE, pygame.Rect(pos[0], pos[1], round(117 * size), round(46 * size)))

    leg((pos[0], pos[1] + round(20 * size)), size, reverse)
    leg((pos[0] + round(25 * size), pos[1] + round(30 * size)), size, reverse)
    leg((pos[0] + round(68 * size), pos[1] + round(20 * size)), size, reverse)
    leg((pos[0] + round(86 * size), pos[1] + round(35 * size)), size, reverse)

    ellipse(screen, WHITE, pygame.Rect(pos[0] + round(87 * size), pos[1] - round(65 * size), round(34 * size),
                                       round(90 * size)))
    ellipse(screen, WHITE, pygame.Rect(pos[0] + round(93 * size), pos[1] - round((83 * size)), round(41 * size),
                                       round(25 * size)))

    circle(screen, PURPLE, (pos[0] + round(112 * size), pos[1] - round(70 * size)), round(8 * size))
    circle(screen, BLACK, (pos[0] + round(115 * size), pos[1] - round(70 * size)), round(4 * size))
    ellipse(screen, WHITE, pygame.Rect(pos[0] + round(106 * size), pos[1] - round(75 * size), round(6 * size),
                                       round(4 * size)))

    ear1 = [pos[0] + round(96 * size), pos[1] - round(75 * size)]
    polygon(screen, WHITE, [ear1, (ear1[0] - round(15 * size), ear1[1] - round(22 * size)),
                            (ear1[0] + round(10 * size), ear1[1])])
    ear2 = [pos[0] + round(108 * size), pos[1] - round(80 * size)]
    polygon(screen, WHITE,
            [ear2, (ear2[0] - round(15 * size), ear2[1] - round(22 * size)), (ear2[0] + round(10 * size), ear2[1])])


def lama_left(pos, size):
    reverse = True
    pos[0] = round(pos[0] * size)
    pos[1] = round(pos[1] * size)
    ellipse(screen, WHITE, pygame.Rect(pos[0] - round(117 * size), pos[1], round(117 * size), round(46 * size)))

    leg((pos[0], pos[1] + round(20 * size)), size, reverse)
    leg((pos[0] - round(25 * size), pos[1] + round(30 * size)), size, reverse)
    leg((pos[0] - round(68 * size), pos[1] + round(20 * size)), size, reverse)
    leg((pos[0] - round(86 * size), pos[1] + round(35 * size)), size, reverse)

    ellipse(screen, WHITE, pygame.Rect(pos[0] - round(87 * size) - round(34 * size), pos[1] - round(65 * size),
                                       round(34 * size), round(90 * size)))
    ellipse(screen, WHITE, pygame.Rect(pos[0] - round(93 * size) - round(41 * size), pos[1] - round((83 * size)),
                                       round(41 * size), round(25 * size)))

    circle(screen, PURPLE, (pos[0] - round(112 * size), pos[1] - round(70 * size)), round(8 * size))
    circle(screen, BLACK, (pos[0] - round(115 * size), pos[1] - round(70 * size)), round(4 * size))
    ellipse(screen, WHITE, pygame.Rect(pos[0] - round(106 * size) - round(6 * size), pos[1] - round(75 * size),
                                       round(6 * size), round(4 * size)))

    ear1 = [pos[0] - round(96 * size), pos[1] - round(75 * size)]
    polygon(screen, WHITE, [ear1, (ear1[0] + round(15 * size), ear1[1] - round(22 * size)),
                            (ear1[0] - round(10 * size), ear1[1])])
    ear2 = [pos[0] - round(108 * size), pos[1] - round(80 * size)]
    polygon(screen, WHITE,
            [ear2, (ear2[0] + round(15 * size), ear2[1] - round(22 * size)), (ear2[0] - round(10 * size), ear2[1])])


def draw_flower(pos, size, num):
    if num == 9:
        flower_9(pos, size)
    if num == 8:
        flower_8(pos, size)
    if num == 7:
        flower_7(pos, size)
    if num == 6:
        flower_6(pos, size)


def flower_9(pos, size):
    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    param = [15, 7]
    param[0] = round(param[0] * size)
    param[1] = round(param[1] * size)
    ellipse(screen, YELLOW,
            pygame.Rect(pos[0] + round(15 * size), pos[1] + round(6 * size), round(18 * size), round(9 * size)))
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(5 * size), pos[1] + round(2 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(5 * size), pos[1] + round(2 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(1 * size), pos[1] + round(6 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(1 * size), pos[1] + round(6 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(5 * size), pos[1] + round(10 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(5 * size), pos[1] + round(10 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(10 * size), pos[1] + round(12 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(10 * size), pos[1] + round(12 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(15 * size), pos[1] + round(0 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(15 * size), pos[1] + round(0 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(23 * size), pos[1] + round(3 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(23 * size), pos[1] + round(3 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(28 * size), pos[1] + round(5 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(28 * size), pos[1] + round(5 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(25 * size), pos[1] + round(9 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(25 * size), pos[1] + round(9 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(20 * size), pos[1] + round(13 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(20 * size), pos[1] + round(13 * size), param[0], param[1]), 1)


def flower_8(pos, size):
    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    param = [15, 7]
    param[0] = round(param[0] * size)
    param[1] = round(param[1] * size)
    ellipse(screen, YELLOW,
            pygame.Rect(pos[0] + round(15 * size), pos[1] + round(6 * size), round(18 * size), round(9 * size)))
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(5 * size), pos[1] + round(2 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(5 * size), pos[1] + round(2 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(1 * size), pos[1] + round(6 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(1 * size), pos[1] + round(6 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(5 * size), pos[1] + round(10 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(5 * size), pos[1] + round(10 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(15 * size), pos[1] + round(12 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(15 * size), pos[1] + round(12 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(15 * size), pos[1] + round(0 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(15 * size), pos[1] + round(0 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(23 * size), pos[1] + round(3 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(23 * size), pos[1] + round(3 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(28 * size), pos[1] + round(7 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(28 * size), pos[1] + round(7 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(25 * size), pos[1] + round(11 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(25 * size), pos[1] + round(11 * size), param[0], param[1]), 1)


def flower_7(pos, size):
    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    param = [15.5, 7.5]
    param[0] = round(param[0] * size)
    param[1] = round(param[1] * size)
    ellipse(screen, YELLOW,
            pygame.Rect(pos[0] + round(15 * size), pos[1] + round(6 * size), round(18 * size), round(9 * size)))
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(5 * size), pos[1] + round(2 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(5 * size), pos[1] + round(2 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(2 * size), pos[1] + round(8 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(2 * size), pos[1] + round(8 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(10 * size), pos[1] + round(13 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(10 * size), pos[1] + round(13 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(20 * size), pos[1] + round(12 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(20 * size), pos[1] + round(12 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(15 * size), pos[1] + round(0 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(15 * size), pos[1] + round(0 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(23 * size), pos[1] + round(3 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(23 * size), pos[1] + round(3 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(28 * size), pos[1] + round(7 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(28 * size), pos[1] + round(7 * size), param[0], param[1]), 1)


def flower_6(pos, size):
    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    param = [17, 8]
    param[0] = round(param[0] * size)
    param[1] = round(param[1] * size)
    ellipse(screen, YELLOW,
            pygame.Rect(pos[0] + round(15 * size), pos[1] + round(6 * size), round(18 * size), round(9 * size)))
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(5 * size), pos[1] + round(2 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(5 * size), pos[1] + round(2 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(2 * size), pos[1] + round(8 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(2 * size), pos[1] + round(8 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(10 * size), pos[1] + round(13 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(10 * size), pos[1] + round(13 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(20 * size), pos[1] + round(12 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(20 * size), pos[1] + round(12 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(17 * size), pos[1] + round(1 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(17 * size), pos[1] + round(1 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + round(25 * size), pos[1] + round(6 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + round(25 * size), pos[1] + round(6 * size), param[0], param[1]), 1)


def bush(pos, size):
    radius = 100
    circle(screen, L_GREEN, pos, round(radius * size))
    draw_flower((pos[0] - round(5 * size), pos[1] + round(35 * size)), 1.6 * size, randint(6, 9))
    draw_flower((pos[0] - round(70 * size), pos[1] - round(45 * size)), 1.4 * size, randint(6, 9))
    draw_flower((pos[0] - round(30 * size), pos[1] - round(20 * size)), 1.2 * size, randint(6, 9))
    draw_flower((pos[0] + round(10 * size), pos[1] - round(55 * size)), 1.8 * size, randint(6, 9))
    draw_flower((pos[0] - round(75 * size), pos[1] + round(25 * size)), 1.8 * size, randint(6, 9))


pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 706))

# Sky and mountains drawing
rect(screen, SKY, (0, 0, 900, 706))

polygon(screen, GRAY,
        [(0, 216), (60, 73), (104, 172), (172, 93), (297, 282), (389, 88), (419, 122), (490, 130), (570, 250),
         (750, 140), (900, 300), (900, 706), (0, 706)])
polygon(screen, BLACK,
        [(0, 216), (60, 73), (104, 172), (172, 93), (297, 282), (389, 88), (419, 122), (490, 130), (570, 250),
         (750, 140), (900, 300), (900, 706), (0, 706)], 1)

polygon(screen, B_GREEN,
        [(0, 373), (38, 362), (75, 359), (114, 352), (271, 355), (280, 414), (294, 418), (900, 419), (900, 706),
         (0, 706)])
polygon(screen, BLACK,
        [(0, 373), (38, 362), (75, 359), (114, 352), (271, 355), (280, 414), (294, 418), (900, 419), (900, 706),
         (0, 706)], 1)

# Creating bushes
bush([420, 581], 0.7)
bush([650, 530], 0.5)
bush([110, 625], 0.8)
bush([110, 625], 1.4)
bush([440, 400], 0.7)
bush([850, 450], 0.7)

# Drawing lamas
draw_lama([500, 800], 0.7, True)
draw_lama([600, 1000], 0.4, True)
draw_lama([600, 800], 0.5)
draw_lama([-80, 190], 3)
draw_lama([600, 350], 1.5, True)
draw_lama([800, 550], 0.7)
draw_lama([900, 850], 0.7, True)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
