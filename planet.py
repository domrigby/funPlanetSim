
import numpy as np
import numpy.linalg as la

import threading

import time

global G 
G = 6.67430e-11

class planet():

    def __init__(self,ID,pos,vel,mass):

        self.ID = ID

        self.pos = np.array(pos)
        self.vel = np.array(vel)
        self.mass = mass

        self.posList = []


    def updateState(self,deltaT,planetList):

        force = np.array([0,0])
        
        for planet in planetList:
            if self.ID != planet.ID:
                r = planet.pos - self.pos

                rUnit = r/la.norm(r)

                forceVec = (G*self.mass*planet.mass/la.norm(r)**2)*rUnit

                force = np.add(force,forceVec)

        self.acc = force/self.mass

        self.pos = self.pos + np.multiply(self.vel,deltaT) + np.multiply(self.acc,deltaT**(2)/2)
        self.vel = self.vel + np.multiply(self.acc,deltaT)


    def threadedUpdateState(self,deltaT,planetList):
        self.t = threading.Thread(target=self.updateState,args=(deltaT,planetList))
        self.t.start()

    def savePos(self,pos):

        if pos != self.posList[-1]:
            self.posList.append(pos)