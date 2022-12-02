
import numpy as np
import numpy.linalg as la

import time

import pygame

global G 
G = 6.67430e-11

class planet():

    def __init__(self,ID,pos,vel,mass):

        self.ID = ID

        self.pos = np.array(pos)
        self.vel = np.array(vel)
        self.mass = mass


    def updateState(self,deltaT,planetList):

        force = np.array([0,0])
        
        for planet in planetList:
            if self.ID != planet.ID:
                r = planet.pos - self.pos

                rUnit = r/la.norm(r)

                print(r)

                forceVec = (G*self.mass*planet.mass/la.norm(r))*rUnit

                force = np.add(force,forceVec)

        self.acc = force/self.mass

        self.pos = self.pos + np.multiply(self.vel,deltaT) + np.multiply(self.acc,deltaT**(2)/2)
        self.vel = self.vel + np.multiply(self.acc,deltaT)

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

    heightOfScreen = 1000
    widthOfScreen = 1000

    pygame.init()
    screen = pygame.display.set_mode((heightOfScreen,widthOfScreen))

    screen.fill((0,0,255))

    pygame.display.update()

    planetList = []
    planetNum = 0

    while True:

        screen.fill((0,0,255))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    print("Left Mouse key was clicked")
                    	
                    pos = np.array(pygame.mouse.get_pos())

                    planetPos = np.divide(np.multiply(pos,scaleArray),np.array([heightOfScreen,widthOfScreen]))

                    newPlanet = planet(planetNum,planetPos,[0,0],10e10)

                    planetList.append(newPlanet)

                    planetNum += 1
        
        for onePlanet in planetList:
            onePlanet.updateState(1,planetList)

        
        for onePlanet in planetList:
            pixPos = posToPixel(onePlanet.pos,xHeight,yHeight,heightOfScreen,widthOfScreen)
            pygame.draw.circle(screen,(255,0,0),(pixPos[0],pixPos[1]),10)


        pygame.display.update()    
        time.sleep(0.1)

if __name__ == "__main__":
    main()