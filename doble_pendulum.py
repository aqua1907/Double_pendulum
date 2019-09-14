import sys
import pygame
import numpy as np
from numpy import sin, cos


size = width, height = [1300, 900]
white = [255, 255, 255]
black = [0, 0, 0]

clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)

m1 = 20
m2 = 20
r1 = 150
r2 = 150
a1 = np.pi / 6
a2 = np.pi / 3
a1_v = 0
a2_v = 0
g = 1
endPoints = []


def acceleration1():
    exp1 = -g * (2 * m1 + m2) * sin(a1)
    exp2 = -m2 * g * sin(a1 - 2 * a2)
    exp3 = -2 * sin(a1 - a2) * m2
    exp4 = (a2_v*a2_v) * r2 + (a1_v*a1_v) * r1 * cos(a1 - a2)
    den = r1 * (2 * m1 + m2 - m2 * cos(2 * a1 - 2 * a2))
    a1_a = (exp1 + exp2 + exp3 * exp4) / den

    return a1_a


def acceleration2():
    exp1 = 2 * sin(a1 - a2)
    exp2 = (a1_v*a1_v) * r1 * (m1 + m2)
    exp3 = g * (m1 + m2) * cos(a1)
    exp4 = (a2_v*a2_v) * r2 * m2 * cos(a1 - a2)
    den = r2 * (2 * m1 + m2 - m2 * cos(2 * a1 - 2 * a2))
    a2_a = (exp1 * (exp2 + exp3 + exp4)) / den

    return a2_a


def trace(coords):
    for i in range(len(coords) - 1):
        # pygame.draw.line(screen, black,
        #                  (int(coords[i][0]), int(coords[i][1])),
        #                  (int(coords[i+1][0]), int(coords[i+1][1])), 1)
        screen.fill(black, ((coords[i][0], coords[i][1]), (2, 2)))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(white)
    a1_a = acceleration1()
    a2_a = acceleration2()

    x1 = r1 * sin(a1) + width / 2
    y1 = r1 * cos(a1) + height / 5

    x2 = x1 + r2 * sin(a2)
    y2 = y1 + r2 * cos(a2)

    endPoints.append((x2, y2))

    pygame.draw.line(screen, black, (width / 2, height / 5), (int(x1), int(y1)), 2)
    pygame.draw.circle(screen, black, (int(x1), int(y1)), m1)
    pygame.draw.line(screen, black, (int(x1), int(y1)), (int(x2), int(y2)), 2)
    pygame.draw.circle(screen, black, (int(x2), int(y2)), m2)

    trace(endPoints)

    a1_v += a1_a
    a2_v += a2_a
    a1 += a1_v
    a2 += a2_v

    clock.tick(50)
    pygame.display.update()

