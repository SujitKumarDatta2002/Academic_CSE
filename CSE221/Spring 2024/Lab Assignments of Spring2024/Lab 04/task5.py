inp = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 04\input5.txt", "r")
out = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 04\output5.txt", "w")


def bfs(graph, root, dest):
  vis = set()
  q = []
  q.append((root, [root]))
  while q != []:
    cur, nxt = q.pop(0)
    if cur == dest:
      return nxt
    vis.add(cur)
    edges = graph[cur]
    for i in edges:
      if i not in vis:
        q.append((i, nxt+[i]))
  return -1


# Input 01
graph = {}
v,e, dest = list(map(int, inp.readline().split()))
for i in range(v+1):
  graph[i] = []
for j in range(e):
  src, nxt = list(map(int, inp.readline().split()))
  graph[src].append((nxt))
  graph[nxt].append((src))
root = 1
short = bfs(graph, root, dest)
out.write("Output 01\n")
if short != -1:
  out.write("Time: " + str(len(short)-1)+'\n'+"Shortest Path: ")
  out.write(" ".join(list(map(str, short))) + "\n")
else:
  out.write(str(-1)+'\n')


# Input 02
graph = {}
v,e, dest = list(map(int, inp.readline().split()))
for i in range(v+1):
  graph[i] = []
for j in range(e):
  src, nxt = list(map(int, inp.readline().split()))
  graph[src].append((nxt))
  graph[nxt].append((src))
root = 1
short = bfs(graph, root, dest)
out.write("Output 02\n")
if short != -1:
  out.write("Time: " + str(len(short)-1)+'\n'+"Shortest Path: ")
  out.write(" ".join(list(map(str, short))) + "\n")
else:
  out.write(str(-1)+'\n')

# Input 03
graph = {}
v,e, dest = list(map(int, inp.readline().split()))
for i in range(v+1):
  graph[i] = []
for j in range(e):
  src, nxt = list(map(int, inp.readline().split()))
  graph[src].append((nxt))
  graph[nxt].append((src))
root = 1
short = bfs(graph, root, dest)
out.write("Output 03\n")
if short != -1:
  out.write("Time: " + str(len(short)-1)+'\n'+"Shortest Path: ")
  out.write(" ".join(list(map(str, short))) + "\n")
else:
  out.write(str(-1)+'\n')

# Input 04
graph = {}
v,e, dest = list(map(int, inp.readline().split()))
for i in range(v+1):
  graph[i] = []
for j in range(e):
  src, nxt = list(map(int, inp.readline().split()))
  graph[src].append((nxt))
  graph[nxt].append((src))
root = 1
short = bfs(graph, root, dest)
out.write("Output 04\n")
if short != -1:
  out.write("Time: " + str(len(short)-1)+'\n'+"Shortest Path: ")
  out.write(" ".join(list(map(str, short))) + "\n")
else:
  out.write(str(-1)+'\n')

# Input 05
graph = {}
v,e, dest = list(map(int, inp.readline().split()))
for i in range(v+1):
  graph[i] = []
for j in range(e):
  src, nxt = list(map(int, inp.readline().split()))
  graph[src].append((nxt))
  graph[nxt].append((src))
root = 1
short = bfs(graph, root, dest)
out.write("Output 05\n")
if short != -1:
  out.write("Time: " + str(len(short)-1)+'\n'+"Shortest Path: ")
  out.write(" ".join(list(map(str, short))) + "\n")
else:
  out.write(str(-1)+'\n')


inp.close()
out.close()
