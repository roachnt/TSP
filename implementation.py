from brute_force import *
import pandas as pd
import matplotlib.pyplot as plt

bf_file = open("ulysses16.tsp","rU")

graph = []

for line in bf_file:
    arr = line.split()
    index = arr[0]
    x = float(arr[1])
    y = float(arr[2])
    n = Node(x,y)
    graph.append(n)

graph_sizes = []
durations = []

for i in range(1,11):
    start = time.time()
    solution = bf_sol(graph, i)
    end = time.time()
    duration = end - start
    graph_sizes.append(i)
    durations.append(duration)


#plt.plot(np.array(df['Graph Size']), np.array(df['Time']))
plt.plot(graph_sizes, durations, color="red")
plt.show()
