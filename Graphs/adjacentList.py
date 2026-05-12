class Graph:
    """
    Graph represented as an adjacency list.

    Each node maps to a list of (neighbor, weight) tuples.
    """

    def __init__(self):
        self.list = {}

    def add_node(self, node):
        """Add a node with no edges."""
        if node not in self.list:
            self.list[node] = []

    def add_edge(self, src, dst, weight: int = 1, undirected: bool = True):
        """Add an edge between src and dst."""
        self.add_node(src)
        self.add_node(dst)
        self.list[src].append((dst, weight))
        if undirected:
            self.list[dst].append((src, weight))

    def remove_edge(self, src, dst, undirected: bool = True):
        """Remove an edge between src and dst."""
        self.list[src] = [(n, w) for n, w in self.list[src] if n != dst]
        if undirected:
            self.list[dst] = [(n, w) for n, w in self.list[dst] if n != src]

    def has_edge(self, src, dst) -> bool:
        """Check if an edge exists between src and dst."""
        return any(n == dst for n, _ in self.list.get(src, []))

    def neighbors(self, node) -> list:
        """Return all neighbors of a node."""
        return [n for n, _ in self.list.get(node, [])]

    def print_list(self):
        """Pretty-print the adjacency list."""
        for node, edges in self.list.items():
            connections = " -> ".join(f"{n}({w})" for n, w in edges) or "none"
            print(f"  {node}: {connections}")


# --- Example usage ---
if __name__ == "__main__":
    g = Graph()

    g.add_edge("A", "B", weight=3)
    g.add_edge("A", "C", weight=1)
    g.add_edge("B", "D", weight=4)
    g.add_edge("C", "D", weight=2)
    g.add_edge("D", "E", weight=5)

    print("Adjacency List:")
    g.print_list()
    #   A: B(3) -> C(1)
    #   B: A(3) -> D(4)
    #   C: A(1) -> D(2)
    #   D: B(4) -> C(2) -> E(5)
    #   E: D(5)

    print("\nNeighbors of A:", g.neighbors("A"))    # ['B', 'C']
    print("Neighbors of D:", g.neighbors("D"))      # ['B', 'C', 'E']
    print("Has edge A-B?  ", g.has_edge("A", "B"))  # True
    print("Has edge A-E?  ", g.has_edge("A", "E"))  # False

    g.remove_edge("A", "B")
    print("\nAfter removing A-B:")
    print("Has edge A-B?  ", g.has_edge("A", "B"))  # False
    print("Neighbors of A:", g.neighbors("A"))      # ['C']