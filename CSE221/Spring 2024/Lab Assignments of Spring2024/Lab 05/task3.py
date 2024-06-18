inp = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 05\input3_1.txt", "r")
out = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 05\output3_1.txt", "w")

def dfs(u, graph, visited, st):
  visited[u] = 'B'
  for v in graph[u]:
    if visited[v] == 'W':
      dfs(v, graph, visited, st)
  st.append(u)

def transpose(graph):
  trGraph = {}
  for u in graph.keys():
    for v in graph[u]:
      if v not in trGraph.keys():
        trGraph[v] = [u]
      else:
        trGraph[v].append(u)
    if u not in trGraph.keys():
      trGraph[u] = []
  return trGraph

def dfs_scc(n, trGraph, visited, pscc):
  visited[n] = 'B'
  pscc.append(n)

  for v in trGraph[n]:
    if visited[v] == 'W':
      dfs_scc(v, trGraph, visited, pscc)



graph = {}
v,e = list(map(int, inp.readline().split()))
for i in range(v):
  graph[i+1] = []

for j in range(e):
  src, dest = list(map(int, inp.readline().split()))
  graph[src].append((dest))
  if j == 1:
    root = src


st = []
visited = {}
for i in graph:
  visited[i] = 'W'

for i in graph.keys():
  if visited[i] == 'W':
    dfs(i, graph, visited, st)

trGraph = transpose(graph)
scc = []
visited2 = {}
for i in graph:
  visited2[i] = 'W'
while st:
  n = st.pop()
  if visited2[n] == 'W':
    pscc = []
    dfs_scc(n, trGraph, visited2, pscc)
    out.write(" ".join(list(map(str, pscc)))+'\n')

inp.close()
out.close()