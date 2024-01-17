from heapq import heappop, heappush

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        self.graph.setdefault(u, []).append((v, weight))
        self.graph.setdefault(v, []).append((u, weight))

    def dijkstra(self, start):
        heap = [(0, start)]
        distances = {start: 0}
        visited = set()

        while heap:
            current_distance, current_vertex = heappop(heap)

            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            for neighbor, weight in self.graph.get(current_vertex, []):
                distance = current_distance + weight

                if distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = distance
                    heappush(heap, (distance, neighbor))

        return distances

g = Graph()
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 2)
g.add_edge(2, 5, 4)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)

start_vertex = 0
distances = g.dijkstra(start_vertex)

print(f"Minimum distances from vertex {start_vertex}:")
for vertex, distance in distances.items():
    print(f"To vertex {vertex}: {distance}")
