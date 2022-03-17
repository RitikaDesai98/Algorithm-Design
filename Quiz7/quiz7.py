#!/usr/bin/env python
# coding: utf-8

# In[3]:


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
        
class Heap():

    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []

    def newminheapNode(self, v, dist):
        minheapNode = [v, dist]
        return minheapNode

    def swapMinHeapNode(self, a, b):
        t = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = t

    def minHeapify(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < self.size and self.array[left][1] < self.array[smallest][1]:
            smallest = left

        if right < self.size and self.array[right][1] < self.array[smallest][1]:
            smallest = right

        if smallest != idx:
            self.pos[self.array[smallest][0]] = idx
            self.pos[self.array[idx][0]] = smallest

            self.swapMinHeapNode(smallest, idx)

            self.minHeapify(smallest)


    def extractMin(self):

        if self.isEmpty() == True:
            return

        root = self.array[0]

        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode

        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1

        self.size -= 1
        self.minHeapify(0)

        return root

    def isEmpty(self):
        return True if self.size == 0 else False

    def decreaseKey(self, v, dist):


        i = self.pos[v]

        self.array[i][1] = dist

        while i > 0 and self.array[i][1] < self.array[(i - 1) / 2][1]:
            self.pos[self.array[i][0]] = (i - 1) / 2
            self.pos[self.array[(i - 1) / 2][0]] = i
            self.swapMinHeapNode(i, (i - 1) / 2)

            i = (i - 1) / 2;

    def isInminheap(self, v):

        if self.pos[v] < self.size:
            return True
        return False

def main():
    g = Graph(102) 
    rows, cols = (102, 102) 

    df = pd.read_csv('Quiz6_Input_File.csv')
    arr = df.to_numpy()

    g.graph = arr

    g.primMST()
    
if __name__ == "__main__":
    main()


# In[ ]:




