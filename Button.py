import pygame
from Textbox import *


class Button:
    def __init__(self, pos, width, height, text, inactive_color=(255, 0, 0), active_color=(0, 0, 255),
                 fontName="times.ttf", fontsize=20):
        self.pos = pos
        self.width = width
        self.height = height
        self.text = text
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.font = pygame.font.Font(fontName, fontsize)
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.active = False

    def Functionality(self, Tree, key):
        if self.text == "INSERT":
            Tree.addNode(key)
        elif self.text == "SEARCH":
            print(Tree.Search(key))
        elif self.text == "DELETE":
            Tree.DeleteNode(key)

    def ChangeColor(self):
        pass

    def DrawButton(self, window):
        text = self.font.render(self.text, False, (0, 0, 0))
        if self.active:
            self.image.fill(self.active_color)
        else:
            self.image.fill(self.inactive_color)
        window.blit(self.image, self.pos)
        window.blit(text, (self.pos[0] + self.width / 6, self.pos[1] + self.height / 3))

    def OnClick(self, Tree, Textbox):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and len(Textbox.text) > 0:
            self.active = True
            self.Functionality(Tree, int(Textbox.text))
        else:
            self.active = False
