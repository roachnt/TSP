import numpy as np
import sys
import time

bf_file = open("ulysses16.tsp","rU")

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%f,%f)" % (self.x,self.y)

def getDistance(node1,node2):
    x1 = node1.x
    x2 = node2.x
    y1 = node1.y
    y2 = node2.y
    return np.sqrt((x1-x2)**2 + (y1-y2)**2)

def getCycleLength(cycle):
    length = 0
    for i, node in enumerate(cycle):
        if i < len(cycle) - 1:
            length += getDistance(cycle[i],cycle[i+1])
        length += getDistance(cycle[-1], cycle[0])
    return length

def bf_sol(graph, size=len(graph)):

    graph = graph[:size]
    # Max out the "best" distance initially
    full_traversals = {}

    # Create a list of paths to pull from
    path_list = []

    # Add path consisting of only starting node
    start_node = graph[0]
    path_list.append([start_node])

    while (path_list):

        path = path_list.pop()

        if len(path) == len(graph):
            full_traversals[getCycleLength(path)] = path

        for node in graph:
            if node not in path:
                new_path = []
                new_path.extend(path)
                new_path.append(node)
                path_list.append(new_path)


    min_distance = min(full_traversals)
    
    print (end - start)
    return full_traversals[min_distance]
