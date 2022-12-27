
import numpy as np
import numpy.linalg as la

import pygame
import pygame_menu

import math

import time

from planet import planet

from arrow import Arrow

from button import Button

from menu import GameMenu

import threading

def posToPixel(pos,xHeight,yWidth,pixHeight,pixWidth):
    pixPosX = int((pos[0]/xHeight)*pixHeight)
    pixPosY = int((pos[1]/yWidth*pixWidth))

    return np.array([pixPosX,pixPosY])


def main():

    xHeight = 10e4
    yHeight = 10e4

    scaleArray = np.array([xHeight,yHeight])

    groundHeight = 100

    origin = [100,yHeight-groundHeight]

    heightOfScreen = 667
    widthOfScreen = 667

    tic = time.perf_counter()
    timeMultiplier = 1

    pygame.init()
    screen = pygame.display.set_mode((heightOfScreen,widthOfScreen))

    # create text and text surface objects
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(f"Time x{timeMultiplier:0.4f}", True, (0,0,0), (255,0,0))
    textRect = text.get_rect()

    speedText = font.render(f"Planet speed =", True, (255,255,255), (0,0,0))
    speedRect = text.get_rect()
    speedRect.center = (400,16)

    planetList = []
    planetNum = 0

    background = pygame.image.load("space.jpeg")
    planetImg = pygame.image.load("planet.png").convert_alpha()

    mouseDown = False

    arrow = Arrow()

    timeUpButton = Button(
        "Speed up",
        (530, 600),
        font=30,
        bg="navy",
        feedback="You clicked me")

    timeDownButton = Button(
        "Slow down",
        (370, 600),
        font=30,
        bg="navy",
        feedback="You clicked me")

    planetMenu = Button(
        "Planet params",
        (20, 600),
        font=30,
        bg="navy",
        feedback="You clicked me")

    planetParams= GameMenu()

    while True:

        screen.blit(background,(0, 0))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()

                if mouse_presses[0]:
                    mousePos = pygame.mouse.get_pos()
                    if timeUpButton.clicked(mousePos):
                        timeMultiplier *= 2
                    elif timeDownButton.clicked(mousePos):
                        timeMultiplier /= 2
                    elif planetMenu.clicked(mousePos):
                        planetParams.showMenu(screen)
                        pygame.display.update()
                    else:
                        mouseDown = True                	
                        origPos = np.array(mousePos)
                        planetPos = np.divide(np.multiply(origPos,scaleArray),np.array([heightOfScreen,widthOfScreen]))

            elif event.type == pygame.MOUSEBUTTONUP and mouseDown == True:
                mouseDown = False
                endPos = np.array(pygame.mouse.get_pos())
                velVec = (origPos - endPos)*planetParams.speedMult
                newPlanet = planet(planetNum,planetPos,velVec,mass=planetParams.planetMass)
                planetList.append(newPlanet)
                planetNum += 1

        if mouseDown == True:
            newPos = np.array(pygame.mouse.get_pos())
            mouseVec = newPos-origPos
            speed = la.norm(mouseVec*planetParams.speedMult)
            speedText = font.render(f"Planet speed = {speed:0.3f}m/s", True, (255,255,255), (0,0,0))
            screen.blit(speedText,speedRect)
            pygame.draw.polygon(screen, (255, 0, 0), arrow.plot(np.arctan2(mouseVec[1],mouseVec[0])+math.pi,la.norm(mouseVec),origPos))
        
        toc = time.perf_counter()
        timeStep = (toc - tic)*timeMultiplier
        for onePlanet in planetList:
            onePlanet.threadedUpdateState(timeStep,planetList)
        tic = time.perf_counter()


        for onePlanet in planetList: # draw force arrows
            pixPos = posToPixel(onePlanet.pos,xHeight,yHeight,heightOfScreen,widthOfScreen)
            screen.blit(planetImg,(pixPos[0],pixPos[1]))
            # pygame.draw.polygon(screen, (0,255,0), arrow.plotVec(pixPos+np.multiply(np.array(planetImg.get_size()),0.5),np.multiply(onePlanet.acc,10),1))

        timeUpButton.show(screen)
        timeDownButton.show(screen)
        planetMenu.show(screen)

        text = font.render(f"Time x{timeMultiplier:0.2f}", True, (255,255,255), (0,0,0))

        screen.blit(text, textRect)

        pygame.display.update()


        
if __name__ == "__main__":
    main()