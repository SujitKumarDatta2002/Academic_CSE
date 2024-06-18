inp = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 05\input1b_2.txt", "r")
out = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 05\output1b_2.txt", "w")


def tropoSortBFS(u, graph, visited, queue, indegree, tropOrder):
  if indegree[u] == 0:
    queue.append(u)
  visited[u] = 'B'
  while queue:
    elm = queue.pop(0)
    tropOrder.append(elm)
    for j in graph[elm]:
      indegree[j]-=1
      if visited[j] == 'W':
        visited[j] = 'B'
      if indegree[j] == 0:
        queue.append(j)


flag = True

graph = {}
v,e = list(map(int, inp.readline().split()))
for i in range(v):
  graph[i+1] = []

for j in range(e):
  src, dest = list(map(int, inp.readline().split()))
  graph[src].append((dest))
  if j == 1:
    root = src

visited = {}
indegree = {}
for i in graph.keys():
  visited[i] = 'W'
  indegree[i] = 0

for j in graph.values():
  for k in j:
    indegree[k] += 1
if 0 not in indegree.values():
  flag = False
queue = []
tropOrder = []
for u in graph.keys():

  if visited[u]=='W' and indegree[u] == 0 and flag == True:

    tropoSortBFS(u, graph, visited, queue, indegree, tropOrder)

if 'W' in visited.values():
    flag = False

if flag == True:
  out.write(" ".join(list(map(str, tropOrder))))
else:
  out.write('IMPOSSIBLE')
inp.close()
out.close()
