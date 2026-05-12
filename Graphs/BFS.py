# def bfs(graph: dict, start: str) -> list:
#     """
#     Breadth-First Search traversal of a graph.
 
#     Args:
#         graph: Adjacency list as a dict {node: [neighbors]}
#         start: Starting node
 
#     Returns:
#         List of nodes in BFS order
#     """
#     visited = set()
#     queue = [start]
#     order = []
#     index = 0  # pointer to the front of the queue
 
#     visited.add(start)
 
#     while index < len(queue):
#         node = queue[index]
#         index += 1
#         order.append(node)
 
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append(neighbor)
 
#     return order





from collections import deque

def bfs(graph:dict, start:str) -> list:

    visited = set()
    queue = deque([start])
    order = []

    visited.add(start)

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return order



graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

print(bfs(graph, 'B'))


