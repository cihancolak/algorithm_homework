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
