def findP(parent, n):
  if parent[n] == n:
    return n
  else:
    return findP(parent, parent[n])

def union(parent, edge, i, j):
  parentI = findP(parent, i)

  parentJ = findP(parent, j)

  if parentI != parentJ:
    countPI = 0
    countPJ = 0
    for k in parent.values():
            if k == parentI:
                countPI += 1
            elif k == parentJ:
                countPJ += 1
    if countPI < countPJ:
            parent[i] = parentJ
    else:
            parent[j] = parentI
    return edge
  return 0


inp1 = open("input1.txt","r")
out1 = open("output1.txt","w")

line1 = inp1.readline().split(' ')
N = int(line1[0])
M = int(line1[1])
graph1 = {}
for i in range(1, N+1):
  graph1[i] = []
lst = inp1.readlines()
start = 0
for i in lst:

    x = i.split(' ')

    key = int(x[0])
    val = [(int(x[1]),int(x[2]))]


    graph1[key] += val


parent = {}
for i in range(1, N+1):
  parent[i] = i


edgedict = {}
edgelist = []
for i in graph1:
  for j in graph1[i]:
    if j[1] not in edgedict.keys():
      edgedict[j[1]] = [(i, j[0])]
      edgelist.append(j[1])
    else:
      edgedict[j[1]] += [(i, j[0])]
      edgelist.append(j[1])



edgelist.sort()

sortededge = {}

for i in edgelist:
  sortededge[i] = edgedict[i]


mincount = 0
for edge in sortededge:
  for nodes in sortededge[edge]:
    mincount += union(parent, edge, nodes[0], nodes[1])

out1.write(str(mincount))
inp1.close()
out1.close()
