
import numpy as np
import pygame

from planet import planet

def posToPixel(pos,xHeight,yWidth,pixHeight,pixWidth):
    pixPosX = int((pos[0]/xHeight)*pixHeight)
    pixPosY = int((pos[1]/yWidth*pixWidth))

    return np.array([pixPosX,pixPosY])

def main():

    xHeight = 1000
    yHeight = 1000

    scaleArray = np.array([xHeight,yHeight])

    groundHeight = 100

    origin = [100,yHeight-groundHeight]

    heightOfScreen = 667
    widthOfScreen = 667

    pygame.init()
    screen = pygame.display.set_mode((heightOfScreen,widthOfScreen))

    planetList = []
    planetNum = 0

    background = pygame.image.load("space.jpeg")
    planetImg = pygame.image.load("planet.png").convert_alpha()

    #planetImg = pygame.transform.scale(screen,(500,500))

    #planetImg = planetImg.convert_alpha()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    	
                    pos = np.array(pygame.mouse.get_pos())

                    planetPos = np.divide(np.multiply(pos,scaleArray),np.array([heightOfScreen,widthOfScreen]))

                    newPlanet = planet(planetNum,planetPos,[0,0],10e10)

                    planetList.append(newPlanet)

                    planetNum += 1
        
        for onePlanet in planetList:
            onePlanet.updateState(1,planetList)

        screen.blit(background,(0, 0))

        for onePlanet in planetList:
            pixPos = posToPixel(onePlanet.pos,xHeight,yHeight,heightOfScreen,widthOfScreen)
            #pygame.draw.circle(screen,(255,0,0),(pixPos[0],pixPos[1]),10)
            screen.blit(planetImg,(pixPos[0],pixPos[1]))

        pygame.display.flip()

if __name__ == "__main__":
    main()