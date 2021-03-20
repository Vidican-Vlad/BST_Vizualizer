from Node import BST
import pygame
from Textbox import Textbox
from Draw import *
import random
from Button import *



#SETUP AND GLOBAL VARIABLES
pygame.init()
tree = BST()
(width, height) = (1900, 1000)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('vizualiator Binary Search Tree  @Vlad Vidican')
font = pygame.font.Font("times.ttf", 10)
OFFSET = 200
stdBtton = (50, 930, 150, 50)
INS = Button((stdBtton[0] + OFFSET, stdBtton[1]), stdBtton[2], stdBtton[3], "INSERT", (156, 76, 76), (255, 0, 0))
SH = Button((stdBtton[0] * 2 + stdBtton[2] + OFFSET, stdBtton[1]), stdBtton[2], stdBtton[3], "SEARCH", (156, 76, 76),
            (255, 0, 0))
MIN = Button((stdBtton[0] * 3 + stdBtton[2]*2 + OFFSET, stdBtton[1]), stdBtton[2], stdBtton[3], "MIN NODE", (156, 76, 76),
            (255, 0, 0))
T = Textbox((stdBtton[0] * 4 + stdBtton[2] * 3 + OFFSET, stdBtton[1]), stdBtton[2], stdBtton[3])
MAX = Button((stdBtton[0] * 5 + stdBtton[2] * 4 + OFFSET, stdBtton[1]), stdBtton[2], stdBtton[3], "MAX NODE", (156, 76, 76),
            (255, 0, 0))
DEL = Button((stdBtton[0] * 6 + stdBtton[2] * 5 + OFFSET, stdBtton[1]), stdBtton[2], stdBtton[3], "DELETE",
             (156, 76, 76), (255, 0, 0))
GEN = Button((stdBtton[0] * 7 + stdBtton[2] * 6 + OFFSET, stdBtton[1]), stdBtton[2], stdBtton[3], "GENERATE",
             (156, 76, 76), (255, 0, 0))
x = None
running = True


def Search():
    global SH,x
    if SH.rect.collidepoint(pygame.mouse.get_pos()) and len(T.text) > 0:
        x = int(T.text)
        SH.active = True
    else:
        SH.active = False
        x = None

def Min():
    global MIN,SH,x,tree
    if MIN.rect.collidepoint(pygame.mouse.get_pos()):
        MIN.active = True
        x = tree.getMIN()
    else:
        if  SH.rect.collidepoint(pygame.mouse.get_pos()) == False:
            MIN.active = False
            x = None

def Max():
    global MAX,SH,MIN,x,tree
    if MAX.rect.collidepoint(pygame.mouse.get_pos()):
        MAX.active = True
        x = tree.getMAX()
    else:
        if (MIN.rect.collidepoint(pygame.mouse.get_pos()) or SH.rect.collidepoint(pygame.mouse.get_pos()) ) == False:
            MAX.active = False
            x = None

def Generate():
    global GEN, tree
    if GEN.rect.collidepoint(pygame.mouse.get_pos()):
        GEN.active = True
        tree = BST()
        for i in range(7):
            tree.addNode(random.randint(0, 100))


#Main Loop
while running:
    #backgound
    screen.fill((105, 105, 105))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Generate()
            Search()
            Min()
            Max()
            INS.OnClick(tree, T)
            DEL.OnClick(tree, T)
            T.checkClick()

        if event.type == pygame.MOUSEBUTTONUP:
            T.checkClick()
            INS.active = False
            SH.active = False
            DEL.active = False
            GEN.active = False
            MAX.active = False
            MIN.active = False
        if event.type == pygame.KEYDOWN:
            x = T.handleInput(event.key)

#Drawing & updating screen
    T.drawTextbox(screen)
    T.drawText(screen)
    DEL.DrawButton(screen)
    INS.DrawButton(screen)
    SH.DrawButton(screen)
    GEN.DrawButton(screen)
    MIN.DrawButton(screen)
    MAX.DrawButton(screen)
    DisplayTree(tree, screen, tree.height, x)
    pygame.display.flip()
