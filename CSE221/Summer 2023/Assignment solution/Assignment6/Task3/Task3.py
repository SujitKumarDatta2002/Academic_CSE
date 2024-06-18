def heapify(arr, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l][0] < arr[smallest][0]:
        smallest = l

    if r < n and arr[r][0] < arr[smallest][0]:
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


def dijkstra(start, graph, n, visited, distance, prev):

    distance[start] = 0
    pq = [(0, start)]

    while pq:

        d, u = deleteNode(pq, 0)
        visited[u] = True
        if d > distance[u]:
            continue

        for v, w in graph[u]:

            new_dist = max(distance[u], w)
            if new_dist < distance[v]:
                distance[v] = new_dist
                addElement(pq, (new_dist, v))

    if distance[n] == float('inf'):
        return 'Impossible'
    return str(distance[n])


inp3 = open("input3.txt", "r")
out3 = open("output3.txt", "w")

line1 = inp3.readline().split(' ')
M = int(line1[0])
N = int(line1[1])
graph3 = {}
for i in range(1, M + 1):
    graph3[i] = []
lst = inp3.readlines()

for i in lst:
    x = i.split(' ')

    key = int(x[0])
    val = [(int(x[1]), int(x[2]))]

    graph3[key] += val

distance = [float('inf')] * (N + 1)
visited = {}
prev = {}
for i in graph3.keys():
    if i not in visited.keys():

        visited[i] = False
        prev[i] = None

out3.write(dijkstra(1, graph3, M, visited, distance, prev))

inp3.close()
out3.close()