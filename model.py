# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 16:30:24 2022

@author: doujialiang
"""

import random
import matplotlib.pyplot as plt
import matplotlib.animation
import csv
import agentframework
import tkinter as tk #Creating GUI
  
random.seed(0)

num_of_wolves = 2#number of wolves
num_of_agents = 10#number of sheep
num_of_iterations = 10
neighbourhood = 20#number of neighbourhood
MaxBound = 99 #max boundary for fig
wolfspeed = 2
agents = []#list for store agents
wolves = []#list for store wolves
fig = matplotlib.pyplot.figure(figsize=(7, 7))#init fig
ax = fig.add_axes([0, 0, 1, 1])

#read environment file
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

environment = []
for row in reader: # A list of rows
    rowlist = []    
    for value in row: # A list of value
        rowlist.append(value)
    environment.append(rowlist)
        
f.close() 

# Make the agents.
for i in range(num_of_agents):
      agents.append(agentframework.Agent(i,environment,agents))
      # print(agents[i])
# Make the wolves
for j in range(num_of_wolves):
     wolves.append(agentframework.Wolf(environment, agents))
#function for wolves kill sheeps 
def kill(self, agents):#put class wolve as self when generating this function
     global num_of_agents # call for the global variable n_o_a cuz need this var to be changed by the function
     for agent in self.prey: #For every sheep
        if agent.x == self.x and agent.y == self.y: # If this sheep shares a range with the wolf
            agents.remove(agent) # remove the sheep
            num_of_agents -=  1 # decrease the number of total sheep
            print("Sheep Eaten!") 
            if num_of_agents == 0:
                print ("All sheep eaten!!!")
def update(self):# main function for animation
    
    fig.clear()
    
    for i in range(num_of_agents):#generating the main functions in class agent
   
        agents[i].eat()
        
        agents[i].move()
        
        
        agents[i].share_with_neighbours(neighbourhood) 

    for j in range(num_of_wolves): #generating the main functions in class wolves
        
        wolves[j].move( MaxBound,wolfspeed,num_of_agents)
        kill(wolves[j],agents) 

    
    for k in range(num_of_agents): #every sheep
        for z in range(num_of_wolves): #And every wolf
            matplotlib.pyplot.ylim(0, 99) #limit y axis to environment
            matplotlib.pyplot.xlim(0, 99) #limit x axis to environment
            matplotlib.pyplot.imshow(environment, alpha=0.8) #plot environment
            matplotlib.pyplot.scatter(agents[k].x,agents[k].y, color = "white") #plot the sheep
            matplotlib.pyplot.scatter(wolves[z].x, wolves[z].y, color = "red") #plot the wolf

# Making GUI:
def start(): #generating the GUI
   animation = matplotlib.animation.FuncAnimation(fig, update, frames=100, repeat=False)
   canvas.draw()
        
def terminate():  #terminate the model
    global root
    root.quit()
    root.destroy()
#Making Buttons:
root = tk.Tk()    
root.wm_title("Wolf-Sheep Model") #Set title

#Create canvas
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create buttons
start_button = tk.Button(root, text="Start Model", command=start) #button to start model
terminate_button = tk.Button(root, text="Stop Model", command=terminate) #button to stop model
start_button.configure(bg='blue') 
terminate_button.configure(bg='red')
#locates the buttons
start_button.pack(side=tk.BOTTOM) 
terminate_button.pack(side=tk.BOTTOM) 

tk.mainloop() #load      
