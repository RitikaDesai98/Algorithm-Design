#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import time

# function to print path 
def printPath(parent, j):
    if parent[j] == -1:
        print(j, end=" ")
        return
    printPath(parent, parent[j])
    print(j, end=" ")

# function to compute the shortest path using Dijkstra algorithm
def dijkstra(graph, start):
    distances = [float("inf") for _ in range(len(graph))]
    visited = [False for _ in range(len(graph))]

    distances[start] = 0
    parent = [-1 for _ in range(len(graph))]

    while True:

        shortest_distance = float("inf")
        shortest_index = -1
        for i in range(len(graph)):

            if distances[i] < shortest_distance and not visited[i]:
                shortest_distance = distances[i]
                shortest_index = i

        if shortest_index == -1:
            if start == 197:
                print("\n\nTest Case: 1 \nFrom Node: 197 \nTo Node: 27 \nDistance: " + str(distances[27]) + " feet \nShortest Path:")
                printPath(parent, 27)
            if start == 65:
                print("\n\nTest Case: 2 \nFrom Node: 65 \nTo Node: 280 \nDistance: " + str(distances[280]) + " feet \nShortest Path:")
                printPath(parent, 280)
            if start == 187:
                print("\n\nTest Case: 3 \nFrom Node: 187 \nTo Node: 68 \nDistance: " + str(distances[68]) + " feet \nShortest Path:")
                printPath(parent, 68)
            return distances

        for i in range(len(graph[shortest_index])):

            if graph[shortest_index][i] != 0 and distances[i] > distances[shortest_index] + graph[shortest_index][i]:

                distances[i] = distances[shortest_index] + graph[shortest_index][i]
                parent[i] = shortest_index

        visited[shortest_index] = True

# read the input files, create a matrix and call the dijkstra function to compute the shortest path
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
        graph = [[0 for i in range(v)] for j in range(v)]
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                graph[int(row[0])][int(row[1])] = int(row[2])
                line_count += 1

    for i in range(v):
        dijkstra(graph, i)

# calculate runtime of program
if __name__ == "__main__" :
    start = time.time()
    main()
    end = time.time()
    print("\n\nRuntime: " + str(end - start))

