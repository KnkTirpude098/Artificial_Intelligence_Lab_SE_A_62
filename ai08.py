def​ a_star(graph, heuristics, start, goal):​

open​_list = set([start])​

​closed_list = set()​


​# Stores g(n) values (cost from start to node)​ ​g = {node: float('inf') for node in graph}​ ​g[start] = 0​

#​ Stores f(n) = g(n) + h(n)​

​f = {node: float('inf') for node in graph}​

f[start]​ = heuristics[start]​


#​ To reconstruct the path​

parents​ = {start: None}​


while​ open_list:​

#​ Select node with lowest f(n)​

​current = min(open_list, key=lambda node: f[node])​


if​ current == goal:​

​# Reconstruct path​

​path = []​

while​ current:​

path​.append(current)​

​current = parents[current]​

​path.reverse()​

​return path, g[goal]​

