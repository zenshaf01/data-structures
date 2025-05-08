'''
A graph is an abstract concept and is also made up of nodes where the nodes might be connected using pointers, just like list or tree nodes are.


Terminology:

Graphs consist of edges and vertices
Vertex: Each Vertex is also known as a node. Vertices are connected to each other using edges. A vertex can be connected to itself using an edge.
Edge: Edges are pointers that connect the vertices. An edge can be unidirectional or bidirectional. The number of edges in a graph always depends upon the number of vertices.
IF the edges have a direction, the graph is called a directed graph. Otherwise it is an undirected graph. Datastructures like trees, linked lists is a directed graph because the pointers are directed, prev, next etc.
The number of edges in a graph will always be less than or equal to V^2. E <= V^2.

Notes:
It is possible that any node in a graph is not connected to eachother and it would still be considered a graph.
A graph can be represented by many different concerete data structures.
- Matrix
- Adjacency Matrix
- Adjacency List
'''