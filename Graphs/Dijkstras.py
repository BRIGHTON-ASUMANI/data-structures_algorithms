def dijkstra(graph: dict, start: str) -> tuple[dict, dict]:
    """
    Dijkstra's shortest path algorithm.

    Args:
        graph: Adjacency list with weights {node: [(neighbor, weight), ...]}
        start: Starting node

    Returns:
        distances: Shortest distance from start to every node
        previous:  Previous node on the shortest path (for path reconstruction)
    """
    # --- TODO: import a min-heap or implement your own priority queue ---
    # import heapq

    unvisited = set(graph.keys())
    distances = {node: float("inf") for node in graph}
    previous  = {node: None for node in graph}
    distances[start] = 0

    while unvisited:
        # TODO: replace this linear scan with a min-heap for O((V+E) log V)
        current = min(unvisited, key=lambda node: distances[node])

        if distances[current] == float("inf"):
            break  # remaining nodes are unreachable

        unvisited.remove(current)

        for neighbor, weight in graph[current]:
            if neighbor not in unvisited:
                continue

            new_dist = distances[current] + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor] = current

    return distances, previous


def reconstruct_path(previous: dict, start: str, end: str) -> list:
    """
    Reconstruct the shortest path from start to end using the previous map.

    Args:
        previous: Dict returned by dijkstra()
        start:    Start node
        end:      Target node

    Returns:
        Ordered list of nodes from start to end, or [] if no path exists
    """
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if path[0] != start:
        return []  # no path found

    return path


# --- Example usage ---
if __name__ == "__main__":
    # Weighted undirected graph: {node: [(neighbor, weight), ...]}
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("A", 1), ("C", 2), ("D", 6)],
        "C": [("A", 4), ("B", 2), ("D", 3)],
        "D": [("B", 6), ("C", 3)],
    }

    distances, previous = dijkstra(graph, start="A")

    print("Shortest distances from A:", distances)
    # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 6}

    path = reconstruct_path(previous, start="A", end="D")
    print("Shortest path from A to D:", path)
    # Output: ['A', 'B', 'C', 'D']