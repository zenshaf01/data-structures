'''
A graph is an abstract concept and is also made up of nodes where the nodes might be connected using pointers, just like list or tree nodes are.

A graph is made up of nodes and pointers. In graphs you can have any amouint nodes (vertices) and any amount of pointers (edges). The only restrcition is that the amount of edges will always be

Terminology:

Graphs consist of edges and vertices
Vertex: Each Vertex is also known as a node. Vertices are connected to each other using edges. A vertex can be connected to itself using an edge.
Edge: Edges are pointers that connect the vertices. An edge can be unidirectional or bidirectional. The number of edges in a graph always depends upon the number of vertices.
IF the edges have a direction, the graph is called a directed graph. Otherwise it is an undirected graph. Datastructures like trees, linked lists is a directed graph because the pointers are directed, prev, next etc.
The number of edges in a graph will always be less than or equal to V^2. E <= V^2. 
The above formula means that the number of edges will always be less than or equal to the amount of vertices in the graph.

Directed graph:
- A graph whos pointers are directed for example previous and next pointers.
Undirected graph:
- A graph whos pointers are not directed meaning you can go in eaither direction using the edge.

Notes:
It is possible that any node in a graph is not connected to eachother and it would still be considered a graph.
A graph can be represented by many different concerete data structures.
- Matrix (common):
A matrix is a 2 dimensional array which can be used to represent a graph. In a matrix you would have rows and columns. 
A row would be the inner array and the column would be the element inside the inner array
In a matrix the element inside the array represents a vertex and the edge is implecit if 2 vertices do not have a 1 between them
for example matrix = 
[   [0,0,0,0],
    [1,1,0,0], 
    [0,0,0,1], 
    [0,1,0,0]
                ]
0 means free to use , travers
1 means the path is blocked and cannot be traversed

in a matrix you can move left, right, up and down.
Now imagine every 0 being a node and since in a matrix you can move in 4 directions, each 0 can move to another 0 and the 0's which have a 1 between then cannot.
The edges are basically between the elements, IF 2 zeroes are adjacent, this means there is an undirected edge between them. 
A 1 between 2 zeroes mean there is no link between the zeroes throught the 1 since that path is blocked.

- Adjacency Matrix:
Using the same matrix like above,
In an adjacency matrix, the index's of the matrix are actually the nodes instead of the elements being the nodes in the matrix.
In an adjacency matrix the index's of the matrix are nodes / vertices and the elements inside the array represent the edge.
Element with value 0 means no edge between the vertex. 1 means an edge between the vertex. The edge is a directed edge.
for example adjMatrix[v1][v2]

- Adjacency List
Very common representing a graph in a coding interview.
The adjacency list Graph Node would have the following information:
1. Value
2. A list of neighbors: This would a list of pointers to the other nodes / vertices. 
Note that this will only have pointers to other or self vertices which this vertex is connected to according to the graph.
'''

# Adjacency list 
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []