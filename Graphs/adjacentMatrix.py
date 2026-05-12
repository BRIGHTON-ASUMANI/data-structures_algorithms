class Graph:
    """
    Graph represented as an adjacency matrix.

    Matrix[i][j] = weight of edge from node i to node j.
    Matrix[i][j] = 0 means no edge.
    """

    def __init__(self, num_nodes: int, node_labels: list = None):
        self.num_nodes = num_nodes
        self.labels = node_labels or list(range(num_nodes))
        self.index = {label: i for i, label in enumerate(self.labels)}
        # 2D matrix initialised to 0 (no edges)
        self.matrix = [[0] * num_nodes for _ in range(num_nodes)]

    def add_edge(self, src, dst, weight: int = 1, undirected: bool = True):
        """Add an edge between src and dst."""
        i, j = self.index[src], self.index[dst]
        self.matrix[i][j] = weight
        if undirected:
            self.matrix[j][i] = weight

    def remove_edge(self, src, dst, undirected: bool = True):
        """Remove an edge between src and dst."""
        i, j = self.index[src], self.index[dst]
        self.matrix[i][j] = 0
        if undirected:
            self.matrix[j][i] = 0

    def has_edge(self, src, dst) -> bool:
        """Check if an edge exists between src and dst."""
        return self.matrix[self.index[src]][self.index[dst]] != 0

    def neighbors(self, node) -> list:
        """Return all neighbors of a node."""
        i = self.index[node]
        return [self.labels[j] for j, w in enumerate(self.matrix[i]) if w != 0]

    def print_matrix(self):
        """Pretty-print the adjacency matrix."""
        header = "     " + "  ".join(f"{l:>2}" for l in self.labels)
        print(header)
        print("     " + "---" * self.num_nodes)
        for i, row in enumerate(self.matrix):
            row_str = "  ".join(f"{v:>2}" for v in row)
            print(f"  {self.labels[i]:>2} | {row_str}")


# --- Example usage ---
if __name__ == "__main__":
    g = Graph(num_nodes=5, node_labels=["A", "B", "C", "D", "E"])

    g.add_edge("A", "B", weight=3)
    g.add_edge("A", "C", weight=1)
    g.add_edge("B", "D", weight=4)
    g.add_edge("C", "D", weight=2)
    g.add_edge("D", "E", weight=5)

    print("Adjacency Matrix:")
    g.print_matrix()
    #        A   B   C   D   E
    #     ---------------
    #   A |  0   3   1   0   0
    #   B |  3   0   0   4   0
    #   C |  1   0   0   2   0
    #   D |  0   4   2   0   5
    #   E |  0   0   0   5   0

    print("\nNeighbors of A:", g.neighbors("A"))   # ['B', 'C']
    print("Neighbors of D:", g.neighbors("D"))     # ['B', 'C', 'E']
    print("Has edge A-B?  ", g.has_edge("A", "B")) # True
    print("Has edge A-E?  ", g.has_edge("A", "E")) # False

    g.remove_edge("A", "B")
    print("\nAfter removing A-B:")
    print("Has edge A-B?  ", g.has_edge("A", "B")) # False
    print("Neighbors of A:", g.neighbors("A"))     # ['C']