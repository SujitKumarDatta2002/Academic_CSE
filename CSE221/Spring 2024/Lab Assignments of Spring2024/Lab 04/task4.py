inp = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 04\input4.txt", "r")
out = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 04\output4.txt", "w")


def dfs(graph, root, vis):
    global flag
    vis[root] = 1
    for i in graph[root]:
      if vis[i] == 0:
        dfs(graph, i, vis)
      elif vis[root] == 1:
        flag = "YES"
    vis[root] = 0
    return flag


# Input 01
graph = {}
v,e = list(map(int, inp.readline().split()))
for i in range(v+1):
  graph[i] = []

for j in range(e):
  src, dest = list(map(int, inp.readline().split()))
  graph[src].append((dest))
  if j == 1:
    root = src
flag = "NO"
vis = [0]*len(graph)
result = dfs(graph, root, vis)
out.write("Output 01\n")
out.write(result+"\n")

# Input 02
graph = {}
v,e = list(map(int, inp.readline().split()))
for i in range(v+1):
  graph[i] = []

for j in range(e):
  src, dest = list(map(int, inp.readline().split()))
  graph[src].append((dest))
  if j == 1:
    root = src
flag = "NO"
vis = [0]*len(graph)
result = dfs(graph, root, vis)
out.write("Output 02\n")
out.write(result+"\n")


# Input 03
graph = {}
v,e = list(map(int, inp.readline().split()))
for i in range(v+1):
  graph[i] = []

for j in range(e):
  src, dest = list(map(int, inp.readline().split()))
  graph[src].append((dest))
  if j == 1:
    root = src
flag = "NO"
vis = [0]*len(graph)
result = dfs(graph, root, vis)
out.write("Output 03\n")
out.write(result+"\n")

# Input 04
graph = {}
v,e = list(map(int, inp.readline().split()))
for i in range(v+1):
  graph[i] = []

for j in range(e):
  src, dest = list(map(int, inp.readline().split()))
  graph[src].append((dest))
  if j == 1:
    root = src
flag = "NO"
vis = [0]*len(graph)
result = dfs(graph, root, vis)
out.write("Output 04\n")
out.write(result+"\n")

# Input 05
graph = {}
v,e = list(map(int, inp.readline().split()))
for i in range(v+1):
  graph[i] = []

for j in range(e):
  src, dest = list(map(int, inp.readline().split()))
  graph[src].append((dest))
  if j == 1:
    root = src
flag = "NO"
vis = [0]*len(graph)
result = dfs(graph, root, vis)
out.write("Output 05\n")
out.write(result+"\n")


inp.close()
out.close()