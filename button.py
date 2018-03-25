import pygame

BLUE = (40, 40, 255)
WHITE = (255,255,255)

class Button():

    def __init__(self, location, size, name):
        self.location = location
        self.size = size
        self.name = name

    def drawButton(self, screen):
        pygame.draw.rect(screen, BLUE, [self.location[0], self.location[1], self.size[0], self.size[1]] )
        pygame.font.init()
        # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
        myfont = pygame.font.SysFont("monospace", 15)

        # render text
        label = myfont.render(self.name, 1, (255,255,0))
        screen.blit(label, (self.location[0] + 10, self.location[1] + 10))
        


