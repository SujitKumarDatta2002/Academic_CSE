def dfs(u, graph, visited, stack):
  visited[u] = 'B'
  for v in graph[u]:
    if visited[v] == 'W':
      dfs(v, graph, visited, stack)
  stack.append(u)

def transpose(graph):
  tr_graph = {}
  for u in graph.keys():
    for v in graph[u]:
      if v not in tr_graph.keys():
        tr_graph[v] = [u]
      else:
        tr_graph[v].append(u)
    if u not in tr_graph.keys():
      tr_graph[u] = []
  return tr_graph

def dfs_scc(n, tr_graph, visited, pscc):
  visited[n] = 'B'
  pscc.append(n)

  for v in tr_graph[n]:
    if visited[v] == 'W':
      dfs_scc(v, tr_graph, visited, pscc)

inp3 = open("input3.txt","r")
out3 = open("output3.txt","w")

line1 = inp3.readline().split(' ')

M = int(line1[0])
N = int(line1[1])
graph3 = {}
for i in range(1, M+1):
  graph3[i] = []
lst2 = inp3.readlines()

for i in lst2:
  x = i.split(' ')

  key = int(x[0])
  val = int(x[1])


  graph3[key].append(val)
  if val not in graph3.keys():
    graph3[val] = []


stack = []
visited = {}
for i in graph3:
  visited[i] = 'W'

for i in graph3.keys():
  if visited[i] == 'W':
    dfs(i, graph3, visited, stack)

tr_graph = transpose(graph3)
scc = []
visited2 = {}
for i in graph3:
  visited2[i] = 'W'
while stack:
  n = stack.pop()
  if visited2[n] == 'W':
    pscc = []
    dfs_scc(n, tr_graph, visited2, pscc)
    rt_str = ''
    for i in pscc:
      rt_str += str(i)
      rt_str += ' '
    out3.write(rt_str+'\n')
inp3.close()
out3.close()
