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

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) +
        ((agents_row_a[1] - agents_row_b[1])**2))**0.5



    
random.seed(0)

num_of_wolves = 2
num_of_agents = 10
num_of_iterations = 10
neighbourhood = 20
MaxBound = 99
wolfspeed = 2
agents = []
wolves = []
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#a = agentframework.Agent()
#b=agentframework.Agent()

#print(a)

#print(b)


f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

environment = []
for row in reader: # A list of rows
    rowlist = []    
    for value in row: # A list of value
        rowlist.append(value)
    environment.append(rowlist)
        
f.close() 
# Don't close until you are done with the reader;
# the data is read on request.



#agents.clear() #ensure blank slate for sheep agent creation
#wolves.clear() #ensure blank slate for wolf agent creation
# Make the agents.
for i in range(num_of_agents):
#     agents.append([random.randint(0,99),random.randint(0,99)])
#     agents.append(agentframework.Agent(3,2))#这行代码更为简单的代替了上行代码，只需要在Agent里面写好
      agents.append(agentframework.Agent(i,environment,agents))
      # print(agents[i])
for j in range(num_of_wolves):
     wolves.append(agentframework.Wolf(environment, agents))
 
def kill(self, agents):
     global num_of_agents # Allows function to edit the sheep number globally (prevents indices error when a sheep has been killed)
     for agent in self.prey: #For every sheep
        if agent.x == self.x and agent.y == self.y: # If this sheep shares a space with the wolf
            agents.remove(agent) # remove sheep from sheep list
            num_of_agents -=  1 # reduce sheep count by one
            print("Sheep Eaten!") # notification of successful kill
            if num_of_agents == 0:
                print ("All sheep eaten!!!")
def update(self):
    
    fig.clear()
    
    for i in range(num_of_agents):
   
        agents[i].eat()
        
        agents[i].move()
        
        
        agents[i].share_with_neighbours(neighbourhood) 
        
        # print(agents[i])
    for j in range(num_of_wolves):
        
        wolves[j].move( MaxBound,wolfspeed,num_of_agents)
        kill(wolves[j],agents) 
        # if random.random() < 0.5:
        #     agents[i][0] = (agents[i][0] + 1) % 100
        # else:
        #     agents[i][0] = (agents[i][0] - 1) % 100

        # if random.random() < 0.5:
        #     agents[i][1] = (agents[i][1] + 1) % 100
        # else:
        #     agents[i][1] = (agents[i][1] - 1) % 100
    
    
    for k in range(num_of_agents): #For every sheep
        for z in range(num_of_wolves): #And every wolf
            matplotlib.pyplot.ylim(0, 99) #limit y axis to environment
            matplotlib.pyplot.xlim(0, 99) #limit x axis to environment
            matplotlib.pyplot.imshow(environment, alpha=0.8) #plot environment
            matplotlib.pyplot.scatter(agents[k].x,agents[k].y, color = "white") #plot the sheep
            matplotlib.pyplot.scatter(wolves[z].x, wolves[z].y, color = "red") #plot the wolf

    # Move the agents.
    #for i in range(num_of_agents):
        #matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    #matplotlib.pyplot.show()
    
    


    
#animation = matplotlib.animation.FuncAnimation(f,agents[i].move(),interval=1)
#animation = matplotlib.animation.FuncAnimation(fig, update,frames=200,repeat=False)


# for agents_row_a in agents:
#     for agents_row_b in agents:
#         distance = distance_between(agents_row_a, agents_row_b)
# Making GUI:
def start(): #generating
   animation = matplotlib.animation.FuncAnimation(fig, update, frames=100, repeat=False)
   canvas.draw()
        
def terminate():  #terminate the model
    global root
    root.quit()
    root.destroy()
#Making Buttons:
root = tk.Tk()    
root.wm_title("Wolf-Sheep Model") #Set title

#Create canvas for drawing model onto
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create buttons which can call functions. Here I have created a 'run' button
# and a 'stop' button
start_button = tk.Button(root, text="Start Model", command=start) #button to start model
terminate_button = tk.Button(root, text="Stop Model", command=terminate) #button to stop model
start_button.configure(bg='blue') #colours start button green
terminate_button.configure(bg='red') #colours stop button red
start_button.pack(side=tk.BOTTOM) #locates start button at bottom of gui
terminate_button.pack(side=tk.BOTTOM) #locates stop button at bottom of gui

tk.mainloop() #load up GUI       