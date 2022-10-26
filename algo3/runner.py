import csv

from dejkstra_algorithm import find_min_distance

with open('gamsrv_in.csv', 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    N, M = file.readline().rsplit()
    clients = [int(i) for i in file.readline().rsplit()]

    graph = []
    for i in range(int(N)+2):
        graph.append([])

    for line in reader:
        parent_vertex, child_vertex, weight = [int(i) for i in line]
        graph[parent_vertex].append((child_vertex, weight))
        parent_vertex, child_vertex = child_vertex, parent_vertex
        graph[parent_vertex].append((child_vertex, weight))


if __name__ == '__main__':
    min_distance = find_min_distance(int(N), clients, graph, int(M))
    print(min_distance)

    with open('gamsrv_out.csv', 'w') as file:
        writer = csv.writer(file)
        file.write(str(min_distance))