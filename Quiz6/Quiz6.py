#!/usr/bin/env python
# coding: utf-8

# In[43]:


import sys 
import pandas as pd
import numpy as np
  
class Graph():
  
    def __init__(self, nodes): 
        self.V = nodes 
        self.graph = [[0 for column in range(nodes)] for row in range(nodes)] 
  
    def printMST(self, parent): 
        print("Node Node\tDistance")
        weight = 0
        for i in range(1, self.V): 
            print(parent[i], "-", i, "\t\t", self.graph[i][ parent[i] ]) 
            weight = weight + self.graph[i][ parent[i]]
        print("Total Distance: " + str(weight))                   
  

    def minKey(self, key, mstSet): 
  
        min = sys.maxsize
  
        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                minIndex = v 
  
        return minIndex 
  
 
    def primMST(self): 
  
        key = [sys.maxsize] * self.V 
        parent = [None] * self.V 
        key[0] = 0 
        mstSet = [False] * self.V 
        parent[0] = -1  
        result = 0
        for cout in range(self.V): 
            u = self.minKey(key, mstSet) 
  
            mstSet[u] = True
            
            for v in range(self.V): 

                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                        key[v] = self.graph[u][v] 
                        parent[v] = u 
                    
        self.printMST(parent)


# In[45]:


g = Graph(102) 
rows, cols = (102, 102) 

df = pd.read_csv('Quiz6_Input_File.csv')
arr = df.to_numpy()

g.graph = arr

g.primMST()

