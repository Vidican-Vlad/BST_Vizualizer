import pygame
from Node import *

hc = 30
wc = 40
pygame.init()
font = pygame.font.Font("times.ttf", 20)


def DRAW(node, window, pos, key):
    if node.key == key:
        text = font.render(str(node.key), False, (0, 255, 0))
    else:
        text = font.render(str(node.key), False, (255, 0, 0))
    window.blit(text, (pos[0], pos[1]))


def drawLine(node, parent, window):
    pygame.draw.line(window, (255, 0, 0), node, parent)


def drawNode(node, parent, pos, window, height, key):
    ic = pos[0] + 1
    jc = pos[1] * 2
    if parent.key < node.key:
        jc += 1
    if node.Left is not None:
        drawNode(node.Left, node, (ic, jc), window, height, key)
    if node.Right is not None:
        drawNode(node.Right, node, (ic, jc), window, height, key)

    x = (2 * pos[1] + 1) * wc * 2 ** (height - pos[0] - 1)
    y = (2 * pos[0] + 1) * (hc / 2)
    xc = (2 * jc + 1) * wc * 2 ** (height - ic - 1)
    yc = (2 * ic + 1) * (hc / 2)
    drawLine((x, y), (xc, yc), window)
    DRAW(node, window, (xc, yc), key)


def DisplayTree(bst, window, height, key):
    if bst.head is None:
        return
    if bst.head.Left is not None:
        drawNode(bst.head.Left, bst.head, (0, 0), window, height, key)
    if bst.head.Right is not None:
        drawNode(bst.head.Right, bst.head, (0, 0), window, height, key)
    x = wc * 2 ** (height - 1)
    DRAW(bst.head, window, (x, 0), key)
