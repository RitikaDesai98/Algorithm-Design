import csv
import time



def printPath(parent, j, keepCountOfNodes):
    if parent[j] == -1:
        keepCountOfNodes[j] += 1
        return
    printPath(parent, parent[j], keepCountOfNodes)
    keepCountOfNodes[j] += 1


def dijkstra(graph, start, keepCountOfNodes):
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

            for i in range(len(graph)):
                printPath(parent, i, keepCountOfNodes)

            return distances

        for i in range(len(graph[shortest_index])):

            if graph[shortest_index][i] != 0 and distances[i] > distances[shortest_index] + graph[shortest_index][i]:

                distances[i] = distances[shortest_index] + graph[shortest_index][i]
                parent[i] = shortest_index

        visited[shortest_index] = True

def main():
    with open('Problem 1/Project 4_Problem 1_InputData.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                lastVertex = int(row[0])
        v = lastVertex + 1

    with open('Problem 1/Project 4_Problem 1_InputData.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        graph = [[0 for i in range(v)] for j in range(v)]
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                graph[int(row[0])][int(row[1])] = int(row[2])
                line_count += 1

    keepCountOfNodes = [0 for i in range(v)]

    for i in range(v):
        dijkstra(graph, i, keepCountOfNodes)
    res = sorted(range(len(keepCountOfNodes)), key=lambda sub: keepCountOfNodes[sub])[-20:]
    res.reverse()
    for i in range(0,len(res)):
        print(str(i+1)+"."+str(res[i]))


if __name__ == "__main__" :
    start = time.time()
    main()
    end = time.time()
    print("\n\nRuntime of the program is " + str(end - start) + "s.")


