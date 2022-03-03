#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import time

# function to print path
def print_path(next_v, u, v):
    p = u
    while (next_v[p][v]):
        print(format(p.get_key()), end = " "),
        p = next_v[p][v]
    print(format(v.get_key()),end = " ")

class Graph:
    def __init__(self):
        # dictionary containing keys that map to the corresponding vertex object
        self.vertices = {}

    def add_vertex(self, key):
        # add a vertex with the given key to the graph
        vertex = Vertex(key)
        self.vertices[key] = vertex

    def get_vertex(self, key):
        # return vertex object with the corresponding key
        return self.vertices[key]

    def __contains__(self, key):
        return key in self.vertices

    def add_edge(self, src_key, dest_key, weight=1):
        # add edge from src_key to dest_key with given weight
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)

    def does_edge_exist(self, src_key, dest_key):
        # return True if there is an edge from src_key to dest_key
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])

    def __iter__(self):
        return iter(self.vertices.values())


class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}

    def get_key(self):
        # return key corresponding to this vertex object
        return self.key

    def add_neighbour(self, dest, weight):
        # make this vertex point to dest with given edge weight
        self.points_to[dest] = weight

    def get_neighbours(self):
        # return all vertices pointed to by this vertex
        return self.points_to.keys()

    def get_weight(self, dest):
        # get weight of edge from this vertex to dest
        return self.points_to[dest]

    def does_it_point_to(self, dest):
        # return True if this vertex points to dest
        return dest in self.points_to

# floyd algorithm to compute shortest path
def floydAlgo(g):

    distance = {v: dict.fromkeys(g, float('inf')) for v in g}
    next_v = {v: dict.fromkeys(g, None) for v in g}

    for v in g:
        for n in v.get_neighbours():
            distance[v][n] = v.get_weight(n)
            next_v[v][n] = n

    for v in g:
        distance[v][v] = 0
        next_v[v][v] = None

    for p in g:
        for v in g:
            for w in g:
                if distance[v][w] > distance[v][p] + distance[p][w]:
                    distance[v][w] = distance[v][p] + distance[p][w]
                    next_v[v][w] = next_v[v][p]

    return distance, next_v

# read input files, call floyd algorithm to compute the shortest path and print
def main():
    g = Graph()

    with open('./Project2_Input_Files/Project2_Input_File3.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                key = int(row[0])
                if key not in g:
                    g.add_vertex(key)

    with open('./Project2_Input_Files/Project2_Input_File3.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                src = int(row[0])
                dest = int(row[1])
                weight = int(row[2])
                if src not in g:
                    print('Vertex {} does not exist.'.format(src))
                elif dest not in g:
                    print('Vertex {} does not exist.'.format(dest))
                else:
                    if not g.does_edge_exist(src, dest):
                        g.add_edge(src, dest, weight)
                    else:
                        print('Edge already exists.')

    distance, next_v = floydAlgo(g)

    i = 0
    for start in g:
        j = 0
        if (i == 197 or i == 65 or i == 187):
            for end in g:
                if (i == 197 and j == 27) or (i == 65 and j == 280) or (i == 187 and j == 68):
                    if (i == 65 and j == 280):
                        print('\n \nTest Case 2')
                    if (i == 197 and j == 27):
                        print('\n \nTest Case 1')
                    if (i == 187 and j == 68):
                        print('\n \nTest Case 3')
                    if next_v[start][end]:
                        print('From Node {} to Node {}: '.format(start.get_key(), end.get_key()))
                        print('Distance {}'.format(distance[start][end]) + ' feet')
                        print('Shortest Path: ')
                        print_path(next_v, start, end)

                j = j + 1
        i = i + 1

# calculate runtime of the program
if __name__ == "__main__" :
    start = time.time()
    main()
    end = time.time()
    print("\n\nRuntime: " + str(end - start))

