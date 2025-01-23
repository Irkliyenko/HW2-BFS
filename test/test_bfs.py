# write tests for bfs
import pytest
import networkx as nx
from search import graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    input_graph = "data/tiny_network.adjlist"

    '''test_graph = nx.Graph()
    test_graph.add_nodes_from(["a", "b", "c", "d", "e", "f", "g", "h"])
    test_graph.add_edges_from([("a", "b"),
    ("a", "c"),
    ("b", "d"),
    ("c", "e"),
    ("c", "f"),
    ("c", "g"),
    ("g", "h")])

    test = graph.Graph(test_graph)
    st = "1"
    test_res = test.bfs(st)
    print(test_res)'''
    # Create the graph object
    g = graph.Graph(input_graph)
    start_node = "Luke Gilbert"

    res = g.bfs(start_node)
    print(res)
    assert len(res) == 30, f"Expected 30 nodes, but got {len(res)}"
     


def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    input_graph = "data/citation_network.adjlist"

    # Create the graph object
    g = graph.Graph(input_graph)

    node_a = "Reza Abbasi-Asl"
    node_b = "34675264"
    node_c = "Nadav Ahituv"

    res_pos = g.bfs(node_a, node_b)
    res_neg = g.bfs(node_a, node_c)
 
    assert res_pos is not None, f"Expected a path between {node_a} and {node_b}, but got None."
    assert res_neg is None, f"Expected None for disconnected nodes, but got {res_neg}."




def test_bfs_edge_cases():

    input_graph = "data/tiny_network.adjlist"

    # Start node
    start_node = "Nadav Ahituv"

    # Edge case: empty graph
    empty_graph = nx.Graph()
    empty_graph = graph.Graph(empty_graph)

    with pytest.raises(ValueError, match="Graph is empty"):
        empty_graph.bfs(start_node)

    ## Create the graph object
    g = graph.Graph(input_graph)

    # Edge case: Start node does not exist
    with pytest.raises(ValueError):
        g.bfs(start="Nonexistent Node")

    # Edge case: End node does not exist
    with pytest.raises(ValueError):
        g.bfs(start_node, end="Nonexistent Node")

    

