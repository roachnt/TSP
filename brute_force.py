import numpy as np


'''
This class will create a node with an x and y coordinate
'''
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%f,%f)" % (self.x, self.y)


'''
Returns the distance between two nodes
'''
def getDistance(node1, node2):
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
    if size <= len(graph):
        graph = graph[:size]

    # Initially, set the smallest path to None
    min_traversal = None

    # Create a list of paths to pull from
    path_list = []

    # Add path consisting of only starting node
    start_node = graph[0]
    path_list.append([start_node])

    # Get all possible traversals
    while path_list:

        # Get path from list
        path = path_list.pop()

        # If it has traversed the entire graph
        # and is smaller than min_traversal,
        # reset min_traversal and skip the loop
        if len(path) == len(graph):
            if min_traversal is None or getCycleLength(path) < getCycleLength(min_traversal):
                min_traversal = path
                continue

        # Otherwise, append a new node to the path
        # and add it to the list of paths to check
        for node in graph:
            if node not in path:
                new_path = []
                new_path.extend(path)
                new_path.append(node)
                path_list.append(new_path)

    # Return the path
    return min_traversal
