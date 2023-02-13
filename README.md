# Uniform Cost Search Algorithm in Python
Uniform Cost Search is a graph search algorithm used in Artificial Intelligence to find the shortest path in a weighted graph. It works by expanding the node with the lowest cost and updating the costs of its neighbors.

The algorithm starts from the starting node and continues expanding nodes until it finds the goal node or all nodes have been explored. The cost of each node is stored and used to determine the order in which nodes are expanded. The node with the lowest cost is expanded first, followed by its neighbors. The costs of the neighbors are updated based on the cost of the current node, and they are added to a priority queue.

The priority queue prioritizes nodes with the lowest cost and ensures that the node with the lowest cost is always expanded next. This way, the algorithm ensures that it finds the shortest path.

The algorithm continues until either the goal node is found or all nodes have been explored. If the goal node is found, the algorithm traces back the path from the goal node to the start node using the parent of each node. If all nodes have been explored, the algorithm returns a failure.

Uniform Cost Search is an optimal algorithm, meaning that it will always find the shortest path if it exists. However, it can be slow if the graph is large, as it may have to explore many nodes before finding the goal node.

## Getting Started

The code can be run using a Python environment such as IDLE or Jupyter Notebook. The code is implemented as a class with one methods: ucs.

## Conclusion

This implementation of ucs algorithm in Python serves as a starting point for further development and understanding of this algorithm. The code can be easily modified for different graph representations or for more specific use cases.
