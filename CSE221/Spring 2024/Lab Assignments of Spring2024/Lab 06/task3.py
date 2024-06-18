import heapq
inp = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 06\input3_2.txt", "r")
out = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 06\output3_2.txt", "w")


def dijkstra(src, graph, distance, visited, v):
    
    distance[src] = 0
    pq = [(src, 0)]
    while pq:
        curr, w = heapq.heappop(pq)
        visited[curr] = True
        if w > distance[curr]:
            continue
        for v, t in graph[curr]:
            new = max(distance[curr], t)
            if new < distance[v]:
                distance[v] = new
                heapq.heappush(pq, (v, distance[v]))

    if distance[v] == float('inf'):
        return "Impossible"
    return str(distance[v])



graph = {}
v,e = list(map(int, inp.readline().split()))
for i in range(v):
    graph[i+1] = []

for j in range(e):
    src, dest, wt = list(map(int, inp.readline().split()))
    graph[src].append((dest, wt))

src = 1
dist = {}
vis = {}
for i in graph.keys():
    if i not in vis.keys():
        dist[i] = float('inf')
        vis[i]  = False
        
out.write(dijkstra(src, graph, dist, vis, v))

inp.close()
out.close()
