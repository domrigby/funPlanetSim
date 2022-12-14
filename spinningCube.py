import pygame
import numpy as np
import math

squareLines = np.array([[[0,0,0],[1,0,0]],[[1,0,0],[1,1,0]],[[1,1,0],[0,1,0]],[[0,1,0],[0,0,0]],
                        [[0,0,1],[1,0,1]],[[1,0,1],[1,1,1]],[[1,1,1],[0,1,1]],[[0,1,1],[0,0,1]]
                        [[0,0,1],[1,0,1]],[[1,0,1],[1,1,1]],[[1,1,1],[0,1,1]],[[0,1,1],[0,0,1]]])

def rotationMatrix(theta) :
    return np.array([[math.cos(theta),-math.sin(theta)],
                       [math.sin(theta), math.cos(theta)]])

def main():

    xHeight = 100000
    yHeight = 100000

    scaleArray = np.array([xHeight,yHeight])

    groundHeight = 100

    origin = [100,yHeight-groundHeight]

    heightOfScreen = 667
    widthOfScreen = 667

    pygame.init()
    screen = pygame.display.set_mode((heightOfScreen,widthOfScreen))

    theta = 0

    while True:

        screen.fill((0,0,0))

        """for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    	pass"""
        
        for line in squareLines:
            newLine = []
            for point in line:
                point = np.multiply(point,100)
                point = np.matmul(rotationMatrix(theta),point)
                point = np.add(point, np.array([widthOfScreen/2,heightOfScreen/2]))
                newLine.append(point)
            pygame.draw.line(screen,(255,0,0),newLine[0], newLine[1])
                
        theta += 0.1

        pygame.display.flip()
        #pygame.display.update()    
        pygame.time.delay(100)

if __name__ == "__main__":
    main()