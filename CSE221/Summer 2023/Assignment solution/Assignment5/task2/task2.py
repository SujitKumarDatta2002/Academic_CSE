def trop_ord_bfs(u, graph, visited, queue, indegree, trop_ord):
  if indegree[u] == 0:
    queue.append(u)
  visited[u] = 'B'
  #for i in graph[u]:
    #indegree[i]-=1
  #trop_ord.append(u)
  while queue:
    elm = queue.pop(0)
    trop_ord.append(elm)
    for j in graph[elm]:
      indegree[j]-=1
      if visited[j] == 'W':
        visited[j] = 'B'
      if indegree[j] == 0:
        queue.append(j)


flag = True
inp2 = open("input2.txt","r")
out2 = open("output2.txt","w")

line1 = inp2.readline().split(' ')

M = int(line1[0])
N = int(line1[1])
graph = {}
startline = inp2.readline().split(' ')
key = int(startline[0])
start = key
val = int(startline[1])
if key not in graph.keys():
    graph[key] = [val]

else:

    graph[key].append(int(val))
lst2 = inp2.readlines()

for i in lst2:
  x = i.split(' ')

  key = int(x[0])
  val = int(x[1])

  if key not in graph.keys():
    graph[key] = [val]

  else:
    graph[key].append(val)
  if val not in graph.keys():
    graph[val] = []

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
trop_ord = []
sortedl = []
for u in graph.keys():

  if visited[u] == 'W' and indegree[u] == 0 and flag == True:
    sortedl.append(u)
sortedl.sort()

for u in sortedl:
  trop_ord_bfs(u, graph, visited, queue, indegree, trop_ord)

if 'W' in visited.values():
  flag = False

if flag == True:
  rt_str = ''
  for i in trop_ord:
    rt_str += str(i) + ' '

  out2.write(rt_str)
else:
  out2.write('IMPOSSIBLE')
inp2.close()
out2.close()