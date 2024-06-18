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
  for i in distance.keys():
    if distance[i] == float('inf'):
      distance[i] = -1
  return distance, prev



inp1 = open("input1.txt","r")
out1 = open("output1.txt","w")

line1 = inp1.readline().split(' ')
M = int(line1[0])
N = int(line1[1])
graph1 = {}
for i in range(1, M+1):
  graph1[i] = []
lst = inp1.readlines()
start = 0
for i in lst:
  if len(i) != 1:
    x = i.split(' ')

    key = int(x[0])
    val = [(int(x[1]),int(x[2]))]


    graph1[key] += val
  else:
    start = int(i)


distance = {}
visited = {}
prev = {}
for i in graph1.keys():
  if i not in visited.keys():
    distance[i] = float('inf')
    visited[i]  = False
    prev[i] = None
rt_str = ''
dijkstra(start, graph1, distance, visited, prev)
for i in distance:
  rt_str += str(distance[i]) + ' '
out1.write(rt_str)
inp1.close()
out1.close()