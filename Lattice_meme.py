class MyClass(object):
    def __init__(self):
        self.color_map=[]


        self.g=nx.grid_2d_graph(10,10,periodic=True)
        for node in g:
            self.g.nodes[node]['color']='green'
    
        #RESTING in green (orange) line, BORED blue and SHARER pink (black)

    
        for node in self.g:
            self.color_map.append(g.nodes[node]['color'])
    
    
        for i in range(5):
            for j in range(5):
    
                if self.g.nodes[i,j]['color'] == 'green':
                    color_choice=random.choices(['pink','green'],[0.001,0.999])[0]
                    self.g.nodes[i,j]['color']=color_choice    
    


    
            for i in range(10):
                for j in range(10):
                    self.g.nodes[i,j]['no']=int(str(i)+str(j))    
     
                    nx.draw(g, node_color=color_map, with labels=True)
                    plt.show()

            def count(self,net,var):
                number=0
                for i in range(sqrt(len(net))):
                    for j in range(sqrt(len(net))):
                        if net.nodes[i,j]['color']==var:
                            number +=1
                return number

def cha():
     color_map=[]
     for node in g:
         if g.nodes[node]['color'] == 'green':
            g.nodes[node]['color']=random.choices(['pink','green'],[0., 0.5])[0]
         if g.nodes[node]['color'] == 'pink' and blue: 
            g.nodes[]
         color_map.append(g.nodes[node]['color'])
     nx.draw(g,node_color=color_map)
     plt.show()
     return


def cha():
     color_map=[]
     for node in g:
         for neighbor in g.neighbors(node):
             if g.nodes[node]['color'] == 'orange':
                 g.nodes[node]['color']=random.choices(['black','orange'],[0.5,0.5])[0]
             elif g.nodes[node]['color'] == 'black' and g.nodes[neighbor]['color']=='orange':
                 g.nodes[node]['color'] = 'orange'
         color_map.append(g.nodes[node]['color'])
     nx.draw(g,node_color=color_map)
     plt.show()
     return


g=nx.grid_2d_graph(10,10,periodic=True)

for node in g:
....:     g.nodes[node]['color']=random.choices(['pink','green','blue'],[0.7,0.2
....: ,0.1])[0]

def count(net,var):
     number=0
     for i in range(sqrt(len(net))):
         for j in range(sqrt(len(net))):
             if net.nodes[i,j]['color']==var:
                 number +=1
     return number


def cha():
....:     color_map=[]
....:     for node in g:
....:         g.nodes[node]['color']='orange'
....:         for neighbor in g.neighbors(node):
....:             if g.nodes[node]['color'] == 'orange':
....:                 g.nodes[node]['color']=random.choices(['black','orange'],[
....: 0.5,0.5])[0]
....:             if g.nodes[node]['color'] == 'black' and random.random() < 0.5
....: :
....:                 if g.nodes[neighbor]['color']=='orange':
....:                     g.nodes[neighbor]['color'] = 'black'
....:                 elif g.nodes[neighbor]['color']=='blue':
....:                     g.nodes[node]['color']='blue'
....:         color_map.append(g.nodes[node]['color'])
....:     nx.draw(g,node_color=color_map)
....:     plt.show()
....:     return


def cha():
     color_map=[]
     for node in g:
         for neighbor in g.neighbors(node):
             if g.nodes[node]['color'] == 'green':
                 g.nodes[node]['color']=random.choices(['pink','green'],[0.001,0.999])[0]
             if g.nodes[node]['color'] == 'pink' and random.random() < 0.01:
                 if g.nodes[neighbor]['color']=='green':
                     g.nodes[neighbor]['color'] = 'pink'
                 elif g.nodes[neighbor]['color']=='blue':
                     g.nodes[node]['color']='blue'
             if g.nodes[node]['color'] == 'blue' and random.random()<0.01:
                 g.nodes[node]['color']='green'
         color_map.append(g.nodes[node]['color'])
     nx.draw(g,node_color=color_map)
     plt.show()
     return
     
     
     
def cha():
     color_map=[]
     for node in g:
         for neighbor in g.neighbors(node):
             if g.nodes[node]['color'] == 'green':
                 g.nodes[node]['color']=random.choices(['pink','green'],[0.001,0.999])[0]
             if g.nodes[node]['color'] == 'pink' and random.random() < 0.01:
                 if g.nodes[neighbor]['color']=='green':
                     g.nodes[neighbor]['color'] = 'pink'
                 elif g.nodes[neighbor]['color']=='blue':
                     g.nodes[node]['color']='blue'
             if g.nodes[node]['color'] == 'blue' and random.random()<0.01:
                 g.nodes[node]['color']='green'
         color_map.append(g.nodes[node]['color'])
     nx.draw(g,node_color=color_map)
     plt.show()
     return     
     
     
     
def run_experiment_n_time_step_m_times(np, m):
....:     for j in range(m):
....:         print("iteration", j)
....:         for i in range(np):
....:             count_rest[i] = count_rest[i] + count(g,'green')
....:             count_share[i] = count_share[i] + count(g,'pink')
....:             count_bored[i] = count_bored[i] + count(g,'blue')
....:             cha()
....:     for i in range(np):
....:         count_rest[i]=count_rest[i]/m
....:         count_share[i] = count_share[i]/m
....:         count_bored[i] = count_bored[i]/m


def original_state(m):
     g=g=nx.grid_2d_graph(m,m,periodic=True)
     for node in g:
         g.nodes[node]['color']=random.choices(['pink','green','blue'],[0.1,0.8,0.1])[0]
     return g

import random 
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

REST = 'green'
SHARER = 'pink'
BORED = 'blue'
#dimension of the 2d lattice network
dimension = 5
#number of times to run the model
nu=5
#function to count the number of a certain color appearing
def count(network,variable):
     number=0
     for i in range(sqrt(len(network))):
         for j in range(sqrt(len(network))):
             if network.nodes[i,j]['color']==variable:
                 number +=1
     return number

#2d square lattice with periodic boundary conditions
def initial_state():
     global g
     global color_map
     g=nx.grid_2d_graph(dimension,dimension,periodic=True)
     #sets color for all nodes as REST (green)
     for node in g:
          g.nodes[node]['color']=REST

     #nodes with chosen colors
     g.nodes[0,0]['color']=SHARER
     g.nodes[2,2]['color']=BORED
     color_map=[]

     #append color into a list
     for node in g:
          color_map.append(g.nodes[node]['color'])

         
#function to carry out 
def change():
     #empty list to append color into
     color_map=[]
     
     for node in g:
         #Neighbor nodes of a given node so up, down, left and right 
         for neighbor in g.neighbors(node):
             if g.nodes[node]['color'] == REST:
               #let a node at rest turn into a sharer with probability 0.001
                 g.nodes[node]['color']=random.choices([SHARER,REST],[0.001,0.999])[0]
              # If node is sharer with probability 0.01 and if neighbor is resting change neighbor into sharer
              # else if neighbor is bored change the node into bored
             if g.nodes[node]['color'] == SHARER and random.random() < 0.01:   
                 if g.nodes[neighbor]['color']==REST:
                     g.nodes[neighbor]['color'] = SHARER
                 elif g.nodes[neighbor]['color']==BORED:
                     g.nodes[node]['color']=BORED
             #If nodes is bored with probability 0.01 and if neighbor is resting change node into rest
             #else node stays bored
             if g.nodes[node]['color'] == BORED and random.random()<0.01:
                  if g.nodes[neighbor]['color']==REST:
                       g.nodes[node]['color']=REST
                  else:
                    g.nodes[node]['color']=BORED
         #append node color into the list "color_map"           
         color_map.append(g.nodes[node]['color'])
     
     return

count_rest =list(range(0,nu))
count_share =list(range(0,nu))
count_bored=list(range(0,nu))


def run_change_n_times(n):
     for j in range(n):
#empty lists to append values of states into  
          initial_state()
          count_rest[j]=[]
          count_share[j]=[]
          count_bored[j]=[]
#append the values into the lists "count_rest", "count_share" and "count_bored"

          for i in range(1000):
               change()
               count_rest[j].append(count(g,REST))
               count_bored[j].append(count(g,BORED))
               count_share[j].append(count(g,SHARER))

run_change_n_times(nu)

#plot the results
fig, ax = plt.subplots()
step = list(range(0,1000))
for i in range(nu):
     
     ax.plot(step,count_rest[i],"#73a832",
     step,count_bored[i],"#3263a8",
     step,count_share[i],"#a832a0")
ax.legend(['Resting', 'Bored', 'Sharer'])
ax.set(xlabel='Time Steps',ylabel='Count of States',title='Spread Of Memes in a 2d square lattice Network')
plt.show()