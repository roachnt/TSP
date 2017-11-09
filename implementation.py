import math
import time
import matplotlib.pyplot as plt
from brute_force import *

bf_file = open('ulysses16.tsp', 'rU')

graph = []

for line in bf_file:
    arr = line.split()
    index = arr[0]
    x = float(arr[1])
    y = float(arr[2])
    n = Node(x, y)
    graph.append(n)

graph_sizes = []
durations = []

for i in range(1,11):
    start = time.time()
    solution = bf_sol2(graph, i)
    end = time.time()
    duration = end - start
    graph_sizes.append(i)
    durations.append(duration)


plt.subplot(2, 1, 1)
plt.plot(graph_sizes, [math.log(i, 10) for i in durations], 'ro-')
plt.title('Time Analysis of Brute Force Implementation')
plt.ylabel('log')
plt.show()