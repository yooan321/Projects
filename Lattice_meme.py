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