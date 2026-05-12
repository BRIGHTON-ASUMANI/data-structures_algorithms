# def dfs_recursive(graph: dict, start: str, visited: set = None) -> list:
#     """
#     Depth-First Search traversal using recursion.
 
#     Args:
#         graph: Adjacency list as a dict {node: [neighbors]}
#         start: Starting node
#         visited: Set of already-visited nodes (used internally)
 
#     Returns:
#         List of nodes in DFS order
#     """
#     if visited is None:
#         visited = set()
 
#     visited.add(start)
#     order = [start]
 
#     for neighbor in graph[start]:
#         if neighbor not in visited:
#             order += dfs_recursive(graph, neighbor, visited)
 
#     return order



def dfs(graph:dict, start:str) -> list:
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)

        for neighbor in reversed(graph[node]): # reversed to preserve left-to-right order
            if neighbor not in visited:
                stack.append(neighbor)

    return order


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

print(dfs(graph, 'C'))