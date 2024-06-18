import heapq

inp = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 06\input2_3.txt", "r")
out = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 06\output2_3.txt", "w")


def dijkstra(u, graph, distance, visited):

    distance[u] = 0
    pq = []
    heapq.heappush(pq, (u, distance[u]))
    while pq:

        n = heapq.heappop(pq)
        if visited[n[0]]:
            continue
        visited[n[0]] = True
        for v in graph[n[0]]:
            alt = distance[n[0]] + v[1]
            if alt < distance[v[0]]:
                distance[v[0]] = alt
                heapq.heappush(pq, (v[0], distance[v[0]]))

    return distance



graph = {}
v,e = list(map(int, inp.readline().split()))
for i in range(v):
    graph[i+1] = []

for j in range(e):
    src, dest, wt = list(map(int, inp.readline().split()))
    graph[src].append((dest, wt))

a, b = list(map(int, inp.readline().split()))

distance1 = {}
visited1 = {}
distance2 = {}
visited2 = {}
for i in graph.keys():
    if i not in visited1.keys() and i not in visited2.keys():
        distance1[i] = float('inf')
        visited1[i]  = False
        distance2[i] = float('inf')
        visited2[i]  = False

dijkstra(a, graph, distance1, visited1)
dijkstra(b, graph, distance2, visited2)


minDist = float('inf')
minDiff = float('inf')
counter = -1
maxTime = 0
for node in range(1, v+1):
    if node in distance1 and node in distance2:
        totalDist = (distance1[node] + distance2[node])
        distDiff = abs(distance1[node] - distance2[node])
        if totalDist < minDist and distDiff < minDiff:

            minDist = totalDist
            minDiff = distDiff

            maxTime = max(distance1[node], distance2[node])
            counter = node

if counter == -1:
    out.write("Impossible")
else:
    out.write(f'Time {maxTime}\nNode {counter}')

inp.close()
out.close()
