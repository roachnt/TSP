from brute_force import *

bf_file = open("ulysses16.tsp","rU")

graph = []

for line in bf_file:
    arr = line.split()
    index = arr[0]
    x = float(arr[1])
    y = float(arr[2])
    n = Node(x,y)
    graph.append(n)

solution = bf_sol(graph, 6)

for node in solution:
    print node
