import heapq
import math

def dijkstra(graph, start):
    distances = {vertex: math.inf for vertex in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, (bandwidth, delay, reliability) in graph[current_vertex].items():
            distance = current_distance + delay 
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def read_input_file(file_path):
    graph = {}
    with open(file_path, 'r') as file:
        adjacency_matrix = []
        delay_matrix = []

        current_matrix = adjacency_matrix

        for line in file:
            if line == '\n':
                current_matrix = delay_matrix if current_matrix is adjacency_matrix else adjacency_matrix
                continue

            data = line.strip().split(':')
            row = [float(value) for value in data[1].split()]
            current_matrix.append(row)

        nodes = range(1, len(adjacency_matrix) + 1)

        for i, node in enumerate(nodes):
            graph[node] = {}

            for j, neighbor in enumerate(nodes):
                delay = delay_matrix[i][j]

                graph[node][neighbor] = (0, delay, 0)  

    return graph

def Solution(file_path, source, destination, bandwidth_requirement, delay_threshold, reliability_threshold):
    graph = read_input_file(file_path)

    distances = dijkstra(graph, source)
    shortest_path = distances[destination]

    if shortest_path == math.inf:
        return "No path found."

    # Check constraints
    if graph[destination][source][0] < bandwidth_requirement:
        return "Bandwidth constraint not satisfied."
    
    if shortest_path > delay_threshold:
        return "Delay constraint not satisfied."
    
    if graph[destination][source][2] < reliability_threshold:
        return "Reliability constraint not satisfied."

    return shortest_path

# Example usage:
file_path = 'your_input_file.txt' 
destination_node = 10
bandwidth_req = 5
delay_thresh = 40
reliability_thresh = 0.70

result = Solution(file_path, source_node, destination_node, bandwidth_req, delay_thresh, reliability_thresh)
print(result)
