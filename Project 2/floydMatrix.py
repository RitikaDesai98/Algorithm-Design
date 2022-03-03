#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import numpy as np
import time

# function to print path
def printpath(p, i, j):
    i, j = int(i), int(j)
    if (i == j):
        print(i, end= " ")
    elif (p[i, j] == -9999999999):
        print (i, '-', j)
    else:
        printpath(p, i, p[i, j]);
        print(j, end= " ")

# floyd's algorithm to compute the shortest path
def floydAlgo(graph, v, p):

    for i in range(0, v):
        for j in range(0, v):
            p[i, j] = i
            if (i != j and graph[i, j] == 0):
                p[i, j] = -9999999999
                graph[i, j] = 9999999999

    for k in range(0, v):
        for i in range(0, v):
            for j in range(0, v):
                if graph[i, j] > graph[i, k] + graph[k, j]:
                    graph[i, j] = graph[i, k] + graph[k, j]
                    p[i, j] = p[k, j]

# read the input file, create a matrix and call floyd's algorithm to calculate shortest path
def main():
    with open('./Project2_Input_Files/Project2_Input_File3.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                lastVertex = int(row[0])
        v = lastVertex + 1

    with open('./Project2_Input_Files/Project2_Input_File3.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        arr = [[0 for i in range(v)] for j in range(v)]
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                arr[int(row[0])][int(row[1])] = int(row[2])
                line_count += 1

    graph = np.array(arr)
    p = np.zeros(graph.shape)
    floydAlgo(graph, v, p)


    print("\n\nTest Case: 1 \nFrom Node: 197 \nTo Node: 27 \nDistance: " + str(graph[197][27]) + " feet \nShortest Path:")
    printpath(p, 197, 27)
    print("\n\nTest Case: 2 \nFrom Node: 65 \nTo Node: 280 \nDistance: " + str(graph[65][280]) + " feet \nShortest Path:")
    printpath(p, 65, 280)
    print("\n\nTest Case: 3 \nFrom Node: 187 \nTo Node: 68 \nDistance: " + str(graph[187][68]) + " feet \nShortest Path:")
    printpath(p, 187, 68)

# calculate runtime of the program
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("\n\nRuntime: " + str(end - start))

