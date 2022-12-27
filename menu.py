import pygame

from button import Button

import time

import math


class GameMenu():

    def __init__(self):
        self.planetMass = 10e6
        self.speedMult = 1

        self.increaseMass = Button(
                "Increase mass",
                (400, 300),
                font=30,
                bg="navy",
                feedback="You clicked me")

        self.decreaseMass = Button(
                "Decrease mass",
                (100, 300),
                font=30,
                bg="navy",
                feedback="You clicked me")

        self.speedUp = Button(
                "Speed up",
                (400, 500),
                font=30,
                bg="navy",
                feedback="You clicked me")

        self.speedDown = Button(
                "Speed down",
                (100, 500),
                font=30,
                bg="navy",
                feedback="You clicked me")
        
        self.quit = Button(
                "Back to sim",
                (270, 600),
                font=30,
                bg="navy",
                feedback="You clicked me")

        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render(f"Mass 10e{math.log(self.planetMass,10):0.4f} kg", True, (0,0,0), (255,0,0))
        self.textRect = self.text.get_rect()
        self.textRect.center = (333,200)

        self.speedFont = pygame.font.Font('freesansbold.ttf', 32)
        self.speedText = self.speedFont.render(f"Speed multiplier: {self.speedMult}", True, (0,0,0), (255,0,0))
        self.speedTextRect = self.speedText.get_rect()
        self.speedTextRect.center = (333,400)

    def showMenu(self,screen):

        menuQuit = False

        while not menuQuit :
            screen.fill((255,255,255))
            self.increaseMass.show(screen)
            self.decreaseMass.show(screen)
            self.speedUp.show(screen)
            self.speedDown.show(screen)
            self.quit.show(screen)

            self.text = self.font.render(f"Mass 1e{math.log(self.planetMass,10):0.0f} kg", True, (0,0,0), (255,0,0))
            self.speedText = self.speedFont.render(f"Speed multiplier: 1e{math.log(self.speedMult,10):0.0f}", True, (0,0,0), (255,0,0))

            screen.blit(self.text, self.textRect)
            screen.blit(self.speedText,self.speedTextRect)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_presses = pygame.mouse.get_pressed()

                    if mouse_presses[0]:
                        mousePos = pygame.mouse.get_pos()
                        if self.decreaseMass.clicked(mousePos):
                            self.planetMass /= 10
                        elif self.increaseMass.clicked(mousePos):
                            self.planetMass *= 10
                        elif self.speedUp.clicked(mousePos):
                            self.speedMult *= 10
                        elif self.speedDown.clicked(mousePos):
                            self.speedMult /= 10
                        elif self.quit.clicked(mousePos):
                            menuQuit = True

