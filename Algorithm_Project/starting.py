import heapq
import math

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'C': 1, 'D': 4},
    'C': {'A': 3, 'B': 1, 'D': 1},
    'D': {'B': 4, 'C': 1}
}

def dijkstra(graph, start):
    distances = {vertex: math.inf for vertex in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def heuristic(node, goal):
    return 0

def astar(graph, start, goal):
    priority_queue = [(0, start)]
    came_from = {}
    cost_so_far = {start: 0}

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            path = []
            while current_node in came_from:
                path.insert(0, current_node)
                current_node = came_from[current_node]
            path.insert(0, start)
            return path

        for neighbor, weight in graph[current_node].items():
            new_cost = cost_so_far[current_node] + weight
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(priority_queue, (priority, neighbor))
                came_from[neighbor] = current_node

    return None

def floyd_warshall(graph):
    vertices = list(graph.keys())
    distances = {i: {j: float('inf') for j in vertices} for i in vertices}

    for i in vertices:
        distances[i][i] = 0
        for neighbor, weight in graph[i].items():
            distances[i][neighbor] = weight

    for k in vertices:
        for i in vertices:
            for j in vertices:
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    return distances

start_vertex = 'A'
end_vertex = 'D'

shortest_distances_dijkstra = dijkstra(graph, start_vertex)
print("Shortest Distances (Dijkstra):", shortest_distances_dijkstra)

shortest_path_astar = astar(graph, start_vertex, end_vertex)
print("Shortest Path (A*):", shortest_path_astar)

shortest_distances_floyd_warshall = floyd_warshall(graph)
print("Shortest Distances (Floyd-Warshall):", shortest_distances_floyd_warshall)
