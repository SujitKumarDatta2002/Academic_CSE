inp = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 05\input1a_1.txt", "r")
out = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 05\output1a_1.txt", "w")

flag = True
def tropologicalSort(n, graph, visited, order, path):
  global flag
  if n not in path:
    path.append(n)
  else:
    flag = False
    return flag
  visited[n] = 'B'
  for i in graph[n]:
    if visited[i] == 'W' and flag == True:
      tropologicalSort(i, graph, visited, order, path)
  x = path.pop(len(path)-1)
  order.append(n)

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
for i in graph.keys():
  visited[i] = 'W'
order = []
path = []
for j in graph.keys():
  if visited[j] == 'W':
    tropologicalSort(j, graph, visited, order, path)

if len(order) !=0:
  order.reverse()
  out.write(" ".join(list(map(str, order))))
else:
  out.write("IMPOSSIBLE")


inp.close()
out.close()
