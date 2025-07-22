import random 
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

REST = 'green'
SHARER = 'pink'
BORED = 'blue'
dimension=10
#function to count the number of a certain color to appear
def count(net,var):
     number=0
     for i in range(sqrt(len(net))):
         for j in range(sqrt(len(net))):
             if net.nodes[i,j]['color']==var:
                 number +=1
     return number
     
     
     



g=nx.grid_2d_graph(dimension,dimension,periodic=True)
for node in g:
    g.nodes[node]['color']=REST
    
g.nodes[0,0]['color']=SHARER
g.nodes[2,2]['color']=BORED
color_map=[]
for node in g:
    color_map.append(g.nodes[node]['color'])

def cha():
     color_map=[]
     for node in g:
         for neighbor in g.neighbors(node):
             if g.nodes[node]['color'] == REST:
                 g.nodes[node]['color']=random.choices([SHARER,REST],[0.001,0.999])[0]
             if g.nodes[node]['color'] == SHARER and random.random() < 0.01:
                 if g.nodes[neighbor]['color']==REST:
                     g.nodes[neighbor]['color'] = SHARER
                 elif g.nodes[neighbor]['color']==BORED:
                     g.nodes[node]['color']=BORED
             if g.nodes[node]['color'] == BORED and random.random()<0.01:
                if g.nodes[neighbor]['color']==REST:
                    g.nodes[node]['color']=REST
                else:
                    g.nodes[node]['color']=BORED
         color_map.append(g.nodes[node]['color'])
     
     return
     
count_rest=[]
count_share=[]
count_bored=[]


def run_change_n_times(n):
    fig,ax = plt.subplots()
    step = list(range(0,1000))
    for j in range(n):
        count_rest=[]
        count_share=[]
        count_bored=[]
        for i in range(1000):
            cha()
            count_rest.append(count(g,REST))
            count_bored.append(count(g,SHARER))
            count_share.append(count(g,BORED))
        ax.plot(step,count_rest,"#73a832", 
                 step,count_bored,"#3263a8", 
                 step,count_share,"#a832a0")   
    ax.legend(['Resting', 'Bored', 'Sharer'])
    ax.set(xlabel='Time Steps',ylabel='Count of States',title='Spread Of Memes in a 2d square lattice Network')
    plt.show()


fig, ax = plt.subplots()
step = list(range(0,1000))
ax.plot(step,count_rest,"#73a832",
step,count_bored,"#3263a8",
step,count_share,"#a832a0")
ax.legend(['Resting', 'Bored', 'Sharer'])
ax.set(xlabel='Time Steps',ylabel='Count of States',title='Spread Of Memes in a 2d square lattice Network')
plt.show()


    
     
Class MemeLattice:
    def __init__(self,dimensions):
        self.p=0.001
        self.q=0.01
        self.r=0.01
        self.dimensions=dimensions
        n_time_steps = 10000
        self.population = dimension
        

