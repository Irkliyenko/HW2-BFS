from collections import deque

import networkx as nx
#import matplotlib.pyplot


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

    def bfs(self, start, queue=None, end=None, visited=None):
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

        # To keep track of visited nodes
        if visited is None:
            visited = set()

        # Initialize the queue
        if queue is None:
            queue = deque([(start, [start])]) 


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
    
    
"""

def main():

    tiny_network = "data/tiny_network.adjlist"


    # Create the graph object
    g = Graph(tiny_network)

    start_node = "Luke Gilbert"
    end_node = "Hani Goodarzi"

    res = g.bfs(start_node, end=end_node)
    print(res)

    # Visualize the graph
    plt.figure(figsize=(10, 6))  # Optional: Adjust figure size
    pos = nx.circular_layout(g.graph)
    nx.draw(g.graph, pos, with_labels=False, node_color="lightblue", node_size=500)
    nx.draw_networkx_labels(g.graph, pos, font_size=8)  # Set smaller font size for labels
    plt.title("Graph Visualization")
    plt.show()

if __name__ == "__main__":

    main()

       


"""



