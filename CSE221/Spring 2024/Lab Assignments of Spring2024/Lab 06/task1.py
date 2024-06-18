import heapq

inp = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 06\input1_1.txt", "r")
out = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 06\output1_1.txt", "w")


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

src = int(inp.readline())
dist = {}
vis = {}
for i in graph.keys():
    if i not in vis.keys():
        dist[i] = float('inf')
        vis[i]  = False

dijkstra(src, graph, dist, vis)

for key, val in dist.items():
    if dist[key] ==  float('inf'):
        dist[key] = -1
out.write(" ".join(list(map(str, list(dist.values())))))
out.write("\n")

inp.close()
out.close()
