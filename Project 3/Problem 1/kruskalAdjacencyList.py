import csv
import time

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []


    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])


    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])


    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)


        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        else:
            parent[yroot] = xroot
            rank[xroot] += 1


    def KruskalMST(self):

        result = []

        i = 0
        e = 0

        self.graph = sorted(self.graph,
                            key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:

            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        edge_count = 0
        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print('Edge {}:({}, {}) cost:{}'.format(edge_count, u, v, weight))
            edge_count += 1
        print("Minimum cost= {}".format(minimumCost))

# function to merge two graphs for adjacency list representation
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

    g.KruskalMST()

if __name__ == "__main__":
    mergeGraph('./Project3_G1_Data.csv', './Project3_G2_Data.csv')








