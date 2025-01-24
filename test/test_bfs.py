from search import graph
import pytest
import networkx as nx


def test_bfs_traversal():
    """
    Test BFS traversal to ensure it explores the correct number of nodes.
    """

    input_graph = "data/tiny_network.adjlist"
    # Create the graph object
    g = graph.Graph(input_graph)
    start_node = "Luke Gilbert"

    # Perform BFS traversal
    res = g.bfs(start_node)
    print(res)
    assert len(res) == 30, f"Expected 30 nodes, but got {len(res)}"
     

def test_bfs():
    """
    Test BFS shortest path for connected and disconnected nodes.
    """
    
    input_graph = "data/citation_network.adjlist"

    # Create the graph object
    g = graph.Graph(input_graph)
    # Test nodes
    node_a = "Reza Abbasi-Asl"
    node_b = "34675264" # Connected node
    node_c = "Nadav Ahituv" # Disconnected node

    # Test path for connected nodes
    res_pos = g.bfs(node_a, node_b)
    # Test path for disconnected nodes
    res_neg = g.bfs(node_a, node_c)
 
    assert res_pos is not None, f"Expected a path between {node_a} and {node_b}, but got None."
    assert res_neg is None, f"Expected None for disconnected nodes, but got {res_neg}."


def test_bfs_edge_cases():
    """
    Test BFS edge cases: empty graph, nonexistent start/end nodes.
    """

    input_graph = "data/tiny_network.adjlist"

    ## Create the graph object
    g = graph.Graph(input_graph)

    # Start node
    start_node = "Nadav Ahituv"

    # Edge case: empty graph
    empty_graph = nx.Graph() # Create empty graph
    empty_graph = graph.Graph(empty_graph)

    with pytest.raises(ValueError, match="Graph is empty"):
        empty_graph.bfs(start_node)

    # Edge case: Start node does not exist
    with pytest.raises(ValueError):
        g.bfs(start="Nonexistent Node")

    # Edge case: End node does not exist
    with pytest.raises(ValueError):
        g.bfs(start_node, end="Nonexistent Node")

    

