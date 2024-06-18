def heapify(arr, n, i):

    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l][1] < arr[smallest][1]:
        smallest = l

    if r < n and arr[smallest][1] > arr[r][1]:
        smallest = r

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)



def addElement(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size // 2) - 1, -1, -1):
            heapify(array, size, i)



def deleteNode(array, idx):
    size = len(array)
    num = array[idx]


    array[idx], array[size - 1] = array[size - 1], array[idx]

    array.pop(size - 1)

    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)

    return num


def dijkstra(u, graph, distance, visited, prev):

  distance[u] = 0
  pq = []
  addElement(pq, (u, distance[u]))
  while pq:

    n = deleteNode(pq, 0)
    if visited[n[0]]:
      continue
    visited[n[0]] = True
    for v in graph[n[0]]:
      alt = distance[n[0]] + v[1]
      if alt < distance[v[0]]:
        distance[v[0]] = alt
        prev[v[0]] = n[0]
        addElement(pq, (v[0], distance[v[0]]))

  return distance, prev


def checkBack(n, prev, start):

  if prev[n] == start:

    return True

  elif prev[n] == None:

    return False
  else:

    if checkBack(prev[n], prev, start):
      return True
inp2 = open("input2.txt","r")
out2 = open("output2.txt","w")

line1 = inp2.readline().split(' ')
N = int(line1[0])
M = int(line1[1])
graph1 = {}
for i in range(1, N+1):
  graph1[i] = []
lst = inp2.readlines()
start1 = 0
start2 = 0
for i in lst:
  if len(i) != 3:
    x = i.split(' ')

    key = int(x[0])
    val = [(int(x[1]),int(x[2]))]


    graph1[key] += val
  else:
    start1 = int(i[0])
    start2 = int(i[2])


distance1 = {}
visited1 = {}
prev1 = {}
distance2 = {}
visited2 = {}
prev2 = {}
for i in graph1.keys():
  if i not in visited1.keys() and i not in visited2.keys():
    distance1[i] = float('inf')
    visited1[i]  = False
    prev1[i] = None
    distance2[i] = float('inf')
    visited2[i]  = False
    prev2[i] = None

dijkstra(start1, graph1, distance1, visited1, prev1)
dijkstra(start2, graph1, distance2, visited2, prev2)


min_dist = float('inf')
min_diff = float('inf')
c_node = -1
s_time = 0
for node in range(1, N+1):
    if node in distance1 and node in distance2:
        total_dist = (distance1[node] + distance2[node])
        dif_dist = distance1[node] - distance2[node]
        if dif_dist < 0:
          dif_dist = -(dif_dist)
        if total_dist < min_dist and dif_dist < min_diff:

            min_dist = total_dist
            min_diff = dif_dist

            s_time = max(distance1[node], distance2[node])
            c_node = node

rt_str = ''
if c_node == -1:
    out2.write("Impossible")
else:
    rt_str = f'Time: {s_time}\nNode: {c_node}'
    out2.write(rt_str)

inp2.close()
out2.close()