import csv
import numpy as np

# function to merge two graphs for adjacency matrix representation
def mergeGraphMatrix(G1,G2):
    with open(G1) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                lastVertex = int(row[0])
        v1 = lastVertex + 1

    with open(G2) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                lastVertex = int(row[0])
        v = v1 + lastVertex + 1

    coordinates_list = []
    with open(G1) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        INF = float('inf')
        arr = [[INF for i in range(v)] for j in range(v)]
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                arr[int(row[0])][int(row[1])] = int(row[2])
                if row[3] not in coordinates_list:
                    coordinates_list.append(row[3])
                line_count += 1

    with open(G2) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if row[3] not in coordinates_list:
                    arr[int(row[0]) + v1][int(row[1]) + v1] = int(row[2])
                if row[3] in coordinates_list:
                    index = coordinates_list.index(row[3])
                    arr[index][int(row[1]) + v1] = int(row[2])
                line_count += 1

    gMatrix = np.array(arr)
    return gMatrix

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

# function to merge two graphs for adjacency list representation
def mergeGraphList(G1,G2):
    with open(G1) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                lastVertex = int(row[0])
        v1 = lastVertex + 1

    with open(G2) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                lastVertex = int(row[0])
        v = v1 + lastVertex + 1

    g = Graph(v)
    coordinates_list = []
    with open(G1) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                g.addEdge(int(row[0]), int(row[1]), int(row[2]) )
                if row[3] not in coordinates_list:
                    coordinates_list.append(row[3])
                line_count += 1

    with open(G2) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if row[3] not in coordinates_list:
                    g.addEdge(int(row[0]) + v1, int(row[1]) + v1, int(row[2]))
                if row[3] in coordinates_list:
                    index = coordinates_list.index(row[3])
                    g.addEdge(index, int(row[1]) + v1, int(row[2]))
                line_count += 1

if __name__ == "__main__":
    mergeGraphMatrix('./Project3_G1_Data.csv', './Project3_G2_Data.csv')
    mergeGraphList('./Project3_G1_Data.csv', './Project3_G2_Data.csv')

