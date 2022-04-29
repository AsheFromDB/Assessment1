# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 12:56:51 2022

@author: doujialiang
"""
import random


class tracking: #for tracking sheep's coordinate when wolves hunting
    def __init__(self, sheepx, sheepy, distance):
        self.distance = distance #stores distance of sheep from wolf
        self.sx = sheepx #stores x coordinate of said sheep
        self.sy = sheepy #stores said sheeps y coordinate

class Agent:#class for sheeps
    
    def __init__(self,ia,environment,agents):
        #self.x=x
        self.id=ia
        self.x=random.randint(0,99)
        # self.x=x
        #self.y=y
        self.y=random.randint(0,99)
        # self.z=random.randint(0,99)
        #print(agents[i])
        
        self.environment = environment
        self.store = 0
        
        self.agents=agents
       

    
    def __str__(self):
       return "id="+ str(self.id)+",y="+ str(self.y)+",x=" + str(self.x)
    
    def move(self):#for sheeps move
        
        
        
        for i in range(10):
            if random.random() < 0.5:
                self.x=(self.x+1)%100
                
            else:
                self.x=(self.x-1)%100
                  
        
            if random.random() < 0.5:
                self.y=(self.y+1)%100
                   
            else:
                self.y=(self.y-1)%100
            
    # def move_coordinate:
    
   
    
    def eat(self): # make sheep eat grass
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10 
            
    def share_with_neighbours(self, neighbourhood):# for sheeps sharing information with each other
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))

    def distance_between(self, agent):# calculating the distance between two objects
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
    
class Wolf: #class for wolves
    def __init__(self, environment, prey):
        self.environment = environment #stores environment data
        self.prey = prey #list fo sheep for interacting (same data as Agent.others)
        self.x = random.randint(0,99) #random x coordinate 
        self.y = random.randint(0,99) #random y coordinate
        
    def distance_between(self, prey):# calculating the distance between wolves and sheeps
        return (((self.x - prey.x)**2) + ((self.y - prey.y)**2))**0.5 
            
    def move(self,MaxBound,wspeed, targets): #for wolves hunting down sheep
     trace = [] # a list for tracking data
     closest =MaxBound 
     for agent in self.prey: #for every sheep
         trace.append(tracking(agent.x, agent.y, self.distance_between( agent))) #storing the coords and distance from a wolf
     for t in range(targets): #for every sheep
         if trace[t].distance < closest: #estimate the distance between this one and wolf and the previous distance
             closest = trace[t].distance #shortest distance to a sheep
     for t in range(targets): #for every sheep
         if closest == trace[t].distance: #if this one is the closest
             if self.x + wspeed < trace[t].sx: #full speed is not enough for increasement
                 self.x += wspeed #increase
             else:
                 if self.x - wspeed > trace[t].sx: #full speed is not enough for decreasement
                     self.x -= wspeed #decrease
                 else:
                     self.x = trace[t].sx #wolves should be within the range
         if closest == trace[t].distance: #repeats for y
             if self.y + wspeed < trace[t].sy:
                 self.y += wspeed
             else:
                 if self.y - wspeed > trace[t].sy:
                     self.y -= wspeed
                 else:
                     self.y = trace[t].sy
                
  

    
