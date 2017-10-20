import numpy as np

'''
This class will create a node with an x and y coordinate
'''
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%f,%f)" % (self.x,self.y)

'''
Returns the distance between two nodes
'''
def getDistance(node1,node2):
    x1 = node1.x
    x2 = node2.x
    y1 = node1.y
    y2 = node2.y
    return np.sqrt((x1-x2)**2 + (y1-y2)**2)

'''
Given a cycle, this provides the total cost of the cycle

cycle, the provided cycle
'''
def getCycleLength(cycle):
    length = 0
    for i, node in enumerate(cycle):
        if i < len(cycle) - 1:
            length += getDistance(cycle[i],cycle[i+1])
        length += getDistance(cycle[-1], cycle[0])
    return length

'''
This is the brute force solution to the traveling salesman problem.

graph, the graph being traversed
size, if you want to reduce the size of the graph to reduce time to solution
'''
def bf_sol(graph, size):

    # Chop size of graph
    if (size <= len(graph)):
        graph = graph[:size]

    # Max out the "best" distance initially
    full_traversals = {}

    # Create a list of paths to pull from
    path_list = []

    # Add path consisting of only starting node
    start_node = graph[0]
    path_list.append([start_node])

    # Get all possible traversals
    while (path_list):

        # Get path from list
        path = path_list.pop()

        # If it has traversed the entire graph,
        # add it to possible solutions
        if len(path) == len(graph):
            full_traversals[getCycleLength(path)] = path
            continue

        # Otherwise, append a new node to the path
        # and add it to the list of paths to check
        for node in graph:
            if node not in path:
                new_path = []
                new_path.extend(path)
                new_path.append(node)
                path_list.append(new_path)

    # Get the minimum distance
    min_distance = min(full_traversals)

    # Return the path
    return full_traversals[min_distance]
