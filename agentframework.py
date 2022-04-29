# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 12:56:51 2022

@author: doujialiang
"""
import random


class tracking: #used for showing wolves the nearest sheeps coordinates
    def __init__(self, sheepx, sheepy, distance):
        self.distance = distance #stores distance of sheep from wolf
        self.sx = sheepx #stores x coordinate of said sheep
        self.sy = sheepy #stores said sheeps y coordinate

class Agent:
    
    def __init__(self,ia,environment,agents):#self.x跟x不是一个东西
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
    
    def move(self):#没有__不是内部函数
        
        
        
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
    
   
    
    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10 
            
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))

    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
    
class Wolf: #used to create wolves
    def __init__(self, environment, prey):
        self.environment = environment #stores environment data
        self.prey = prey #list fo sheep for interacting (same data as Agent.others)
        self.x = random.randint(0,99) #random x coordinate 
        self.y = random.randint(0,99) #random y coordinate
        
    def distance_between(self, prey):
        return (((self.x - prey.x)**2) + ((self.y - prey.y)**2))**0.5 
    
    def kill(self, agents):
     global num_of_agents # Allows function to edit the sheep number globally (prevents indices error when a sheep has been killed)
     for agent in self.prey: #For every sheep
        if agent.x == self.x and agent.y == self.y: # If this sheep shares a space with the wolf
            agents.remove(agent) # remove sheep from sheep list
            num_of_agents -=  1 # reduce sheep count by one
            print("Sheep Eaten!") # notification of successful kill
            if num_of_agents == 0:
                print ("All sheep eaten!!!")
                
    def kill(self, agents):
     global num_of_agents # Allows function to edit the sheep number globally (prevents indices error when a sheep has been killed)
     for agent in self.prey: #For every sheep
        if agent.x == self.x and agent.y == self.y: # If this sheep shares a space with the wolf
            agents.remove(agent) # remove sheep from sheep list
            num_of_agents -=  1 # reduce sheep count by one
            print("Sheep Eaten!") # notification of successful kill
            if num_of_agents == 0:
                print ("All sheep eaten!!!")     
                
    def move(self,MaxBound,wspeed, targets): #function for wolves to hunt down sheep
     trace = [] # create a list for filling with tracking data
     closest =MaxBound #sets the base parameter for shortest distance to a sheep to max possible distance
     for agent in self.prey: #for every sheep
         trace.append(tracking(agent.x, agent.y, self.distance_between( agent))) #create an agent storing said sheeps coordinates and distance from wolf
     for t in range(targets): #for every sheep
         if trace[t].distance < closest: #if this sheep is closer than the previous closest sheep
             closest = trace[t].distance #set this as the shortest distance to a sheep
     for t in range(targets): #for every sheep
         if closest == trace[t].distance: #if this sheep is the closest
             if self.x + wspeed < trace[t].sx: #if full speed wont allow the wolf x coord to increase enough
                 self.x += wspeed #increase x coordinate by max wolf movement
             else:
                 if self.x - wspeed > trace[t].sx: #if full speed wont allow the wolf x coord to decrease enough
                     self.x -= wspeed #decrease x coordinate by wolf full speed
                 else:
                     self.x = trace[t].sx #wolf must be within reach of sheep so move into sheep coordinates
         if closest == trace[t].distance: #repeats move conditions for y coordinates
             if self.y + wspeed < trace[t].sy:
                 self.y += wspeed
             else:
                 if self.y - wspeed > trace[t].sy:
                     self.y -= wspeed
                 else:
                     self.y = trace[t].sy
                
  

    
