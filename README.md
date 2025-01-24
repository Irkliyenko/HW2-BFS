# Assignment 2 - Breadth-first search

---

## Assignment Overview
The purpose of this assignment is to get you comfortable working with graph structures and to implement a breadth-first search function to traverse the graph and find the shortest path between nodes.

---

## Description

The `search/graph.py` script contains the `Graph` class, which initializes a graph from a `.adjlist` file using the NetworkX package. This class also includes the implementation of the **Breadth-First Search (BFS)** algorithm, defined in the `bfs` method.

### Breadth-First Search (`bfs`)

The `bfs` method performs a BFS traversal or finds the shortest path in the graph, depending on the provided arguments.

1. **Visited Set**: 
   - A set named `visited` is created to store nodes that have already been explored.

2. **Queue Initialization**: 
   - A queue is initialized using the `deque` class from the `collections` package.
   - The starting node, which must be provided as an argument to the function, is added to the queue.

3. **Traversal Process**:
   - Nodes are dequeued (removed from the front of the queue) one at a time.
   - If the dequeued node is not in the `visited` set, it is added to the set.
   - If the node already exists in `visited`, the function skips it and moves to the next node in the queue.
   - If the dequeued node matches the optional `end` node argument, the method returns the path leading to that node.
   - Otherwise, the method iterates over the neighbors of the current node. Neighbors that have not yet been visited are added to the queue with the path updated.

4. **Return Values**:
   - If the `end` node is specified and a path is found, the function returns the shortest path to that node.
   - If the `end` node is specified but no path is found, the function returns `None`.
   - If no `end` node is specified, the function returns the full list of visited nodes in BFS traversal order.

### Edge Case Handling

The `bfs` function includes handling for the following edge cases:
- **Empty Graph**: 
  - If the graph is empty, a `ValueError` is raised.
- **Nonexistent Start Node**: 
  - If the starting node is not in the graph, a `ValueError` is raised.
- **Nonexistent End Node**: 
  - If the specified `end` node does not exist in the graph, a `ValueError` is raised.

---

## Unit Tests for `bfs`

The `tests/` folder contains unit tests for the `bfs` method in the `Graph` class. These tests are written using the `pytest` framework to ensure the correctness of BFS traversal, shortest path functionality, and edge case handling.

### Test Descriptions

1. **`test_bfs_traversal`**:
   - Validates that BFS traversal explores the correct number of nodes using the `tiny_network.adjlist` file.

2. **`test_bfs`**:
   - Tests the shortest path functionality for both connected and disconnected nodes using the `citation_network.adjlist` file.

3. **`test_bfs_edge_cases`**:
   - Ensures BFS handles edge cases correctly, including:
     - Empty graph.
     - Nonexistent start node.
     - Nonexistent end node.


