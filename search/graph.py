from collections import deque
import networkx as nx


class Graph:
    """
    Class to contain a graph and your bfs function
    
    """
    def __init__(self, filename: str): 
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None, visited=None):
        """
        Perform a Breadth-First Search (BFS) on the graph.
        """

        # Handle edge cases
        if len(self.graph) == 0:# Edge case: an empty graph
            raise ValueError(f"Graph is empty")
        
        if start not in self.graph: # Edge case: start node does not exist in the graph
            raise ValueError(f"Start node '{start}' does not exist in the graph")
        
        if end is not None and end not in self.graph: # Edge case: end node does not exist
            raise ValueError(f"End node '{end}' is not in the graph")

        
        # Initialize visited set and queue for BFS
        visited = visited or set()
        queue = deque([(start, [start])])  # (current_node, path_to_node)


        while queue:
            current_node, path = queue.popleft()

            # Skip already visited nodes
            if current_node in visited:
                continue
            visited.add(current_node)

            # Return the path if the end node is reached
            if current_node == end:
                return path

            # Add unvisited neighbors to the queue
            for neighbor in self.graph.neighbors(current_node):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

        # Return None if the end node was specified but not reachable
        if end is not None:
            return None

        # Return the BFS traversal order if no end node was specified
        return list(visited)


