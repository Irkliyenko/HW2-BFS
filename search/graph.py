from collections import deque

import networkx as nx


class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str): 
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None, visited=None):
        """
        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None
        """
        # Edge case: an empty graph
        if len(self.graph) == 0:
            raise ValueError(f"Graph is empty")
        
        # Edge case: start node does not exist in the graph
        if start not in self.graph:
            raise ValueError(f"Start node '{start}' does not exist in the graph")
        
        # Edge case: end node does not exist
        if end is not None and end not in self.graph:
            raise ValueError(f"End node '{end}' is not in the graph")

        
        # Initialize visited and queue
        visited = visited or set()
        queue = deque([(start, [start])])  # (current_node, path_to_node)


        while queue:
            current_node, path = queue.popleft()

            # Skip nodes that have already been visited
            if current_node in visited:
                continue
            visited.add(current_node)

            # If an end node is specified and reached, return the path
            if current_node == end:
                return path

            # Add unvisited neighbors to the queue
            for neighbor in self.graph.neighbors(current_node):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

        # If end node was specified but no path exists
        if end is not None:
            return None

        # If no end node was specified, return BFS traversal order
        return list(visited)


def main():
    # Initialize the graph
    tiny_network = "data/tiny_network.adjlist"
    g = Graph(tiny_network)

    # Test BFS traversal
    start_node = "Luke Gilbert"
    print(f"BFS Traversal from {start_node}: {g.bfs(start=start_node)}")

    # Test BFS shortest path
    end_node = "Hani Goodarzi"
    path = g.bfs(start=start_node, end=end_node)
    if path:
        print(f"Shortest path from {start_node} to {end_node}: {path}")
    else:
        print(f"No path exists from {start_node} to {end_node}.")

if __name__ == "__main__":
    main()
