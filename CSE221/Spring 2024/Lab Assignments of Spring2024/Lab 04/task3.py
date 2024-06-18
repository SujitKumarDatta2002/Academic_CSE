from collections import deque
inp = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 04\input3.txt", "r")
out = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 04\output3.txt", "w")


def dfs(graph, root):
  vis = []
  q = []
  q.append(root)
  while q != []:
    deq = q.pop()
    if deq not in vis:
      vis.append(deq)
      edges = graph[deq]
      for i in edges:
        q.append(i)
  return vis

# Input 01
graph = {}
v,e = list(map(int, inp.readline().split()))
for i in range(v+1):
  graph[i] = []

for j in range(e):
  src, dest = list(map(int, inp.readline().split()))
  graph[src].append((dest))
  graph[dest].append((src))
  if j == 0:
    root = src
result = dfs(graph, root)
out.write("Output 1\n")
out.write(" ".join(list(map(str, result)))+"\n")

# Input 02
graph = {}
v,e = list(map(int, inp.readline().split()))
for i in range(v+1):
  graph[i] = []

for j in range(e):
  src, dest = list(map(int, inp.readline().split()))
  graph[src].append((dest))
  graph[dest].append((src))
  if j == 0:
    root = src
result = dfs(graph, root)
out.write("Output 2\n")
out.write(" ".join(list(map(str, result)))+"\n")

# Input 03
graph = {}
v,e = list(map(int, inp.readline().split()))
for i in range(v+1):
  graph[i] = []

for j in range(e):
  src, dest = list(map(int, inp.readline().split()))
  graph[src].append((dest))
  graph[dest].append((src))
  if j == 0:
    root = src
result = dfs(graph, root)
out.write("Output 3\n")
out.write(" ".join(list(map(str, result)))+"\n")

# Input 04
graph = {}
v,e = list(map(int, inp.readline().split()))
for i in range(v+1):
  graph[i] = []

for j in range(e):
  src, dest = list(map(int, inp.readline().split()))
  graph[src].append((dest))
  graph[dest].append((src))
  if j == 0:
    root = src
result = dfs(graph, root)
out.write("Output 4\n")
out.write(" ".join(list(map(str, result)))+"\n")

inp.close()
out.close()