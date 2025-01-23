# write tests for bfs
import pytest
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

    # Create the graph object
    g = graph.Graph(input_graph)
    start_node = "Luke Gilbert"

    res = g.bfs(start_node)

    assert len(res) == 30, 'bfs func does not work'


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
 
    assert res_pos is not None, "Not connected"
    assert res_neg is None, "Someting is wrong"


