import pygame


class Textbox:
    def __init__(self, pos, width, height, active=False, inactive_color=(204, 255, 255),
                 active_color=(0, 204, 204)
                 , fontname="times.ttf", text_size=20, text_color=(0, 0, 0)):
        self.pos = pos
        self.width = width
        self.height = height
        self.active = active
        self.text = ""
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.font = pygame.font.Font(fontname, text_size)
        self.text_size = text_size
        self.text_color = text_color

    def drawTextbox(self, window):
        if self.active:
            self.image.fill(self.active_color)
        else:
            self.image.fill(self.inactive_color)
        window.blit(self.image, self.pos)

    def handleInput(self, key):
        if self.active:
            if key == 8:
                self.text = self.text[:-1]
            elif key in range(48, 58) and len(self.text) <= 3:
                self.text += chr(key)

    def drawText(self, window):
        if self.active:
            text = self.font.render(self.text, False, (0, 0, 0))
            window.blit(text, (self.pos[0] + self.width / 3 + 5, self.pos[1] + self.height / 3))

    def checkClick(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.active = True
        else:
            self.active = False
            self.text = ""
