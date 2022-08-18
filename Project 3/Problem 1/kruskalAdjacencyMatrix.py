import csv
import numpy as np
import time


def find(i, parent):
    while parent[i] != i:
        i = parent[i]
    return i

def union(i, j, parent):
    a = find(i, parent)
    b = find(j, parent)
    parent[a] = b


def kruskalAlgo(cost, parent, V):
    mincost = 0  # Cost of min MST

    for i in range(V):
        parent[i] = i

    edge_count = 0
    print("Edges in the constructed MST")
    while edge_count < V - 1:
        min = float('inf')
        a = -1
        b = -1
        for i in range(V):
            for j in range(V):
                if find(i, parent) != find(j, parent) and cost[i][j] < min:
                    min = cost[i][j]
                    a = i
                    b = j
        union(a, b, parent)
        print('Edge {}:({}, {}) cost:{}'.format(edge_count, a, b, min))
        edge_count += 1
        mincost += min

    print("Minimum cost= {}".format(mincost))

# function to merge two graphs for adjacency matrix representation
def mergeGraph(G1,G2):
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

    graph = np.array(arr)
    return graph

def main():
    graph = mergeGraph('./Project3_G1_Data.csv', './Project3_G2_Data.csv')
    V = len(graph)
    parent = [i for i in range(V)]
    kruskalAlgo(graph, parent, V)

if __name__ == "__main__":
    main()
