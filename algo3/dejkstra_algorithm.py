from queue import PriorityQueue
import sys

graph = None
number_of_vertexes = None
clients = None
vertex_distance = None
parent_vertexes = None
min_distance_to_server = None


def find_min_distance(N, C, G, M):
    global graph
    global number_of_vertexes
    global clients
    global min_distance_to_server

    if (type(N) != int) or (type(M) != int) or (type(C) != list) or (type(G) != list):
        raise TypeError('The number of vertexes/edges must be an integer, the graph must be a list')
    if not ((3 <= N <= 1000) and (2 <= M <= 1000) and (len(C) > 0) and (len(G) > 3)):
        raise ValueError('The number of vertexes must be between 3 and 1000, the number of edges must be between 2 and 1000, '
                         'the number of clients must be al least 1, number of vertexes must be at least 4 (where 2 are extra)')

    min_distance_to_server = sys.maxsize
    number_of_vertexes = N
    graph = G
    clients = C

    for start_vertex in range(1, number_of_vertexes + 1):
        if start_vertex not in clients:
            candidate = dejkstra(graph, start_vertex)
            if candidate < min_distance_to_server:
                min_distance_to_server = dejkstra(graph, start_vertex)
    return min_distance_to_server


def dejkstra(graph: list, start_vertex: int):
    init_graph_vars(graph, start_vertex)

    available_vertexes_queue = PriorityQueue()
    available_vertexes_queue.put((0, start_vertex))

    while not available_vertexes_queue.empty():
        vertex_to_check = available_vertexes_queue.get()[1]
        for child_vertex_tuple in graph[vertex_to_check]:
            child_vertex = child_vertex_tuple[0]
            distance_to_child_vertex = vertex_distance[vertex_to_check] + child_vertex_tuple[1]
            if relax_edge(child_vertex, vertex_to_check, distance_to_child_vertex):
                available_vertexes_queue.put((distance_to_child_vertex, child_vertex))
    return get_max_distance_to_clients()


def relax_edge(child_vertex, parent_vertex, distance):
    if vertex_distance[child_vertex] > distance:
        parent_vertexes[child_vertex] = parent_vertex
        vertex_distance[child_vertex] = distance
        return True
    return False


def init_graph_vars(graph: list, start_vertex: int):
    global vertex_distance
    global parent_vertexes
    vertex_distance = []
    parent_vertexes = []
    for vertex in graph:
        vertex_distance.append(sys.maxsize)
        parent_vertexes.append(None)
    vertex_distance[start_vertex] = 0


def get_max_distance_to_clients():
    distances_to_clients = []
    for client_vertex in clients:
        distances_to_clients.append(vertex_distance[client_vertex])
    return max(distances_to_clients)
