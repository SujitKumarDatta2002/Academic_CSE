
import heapq

inp = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab Evaluation\input.txt", "r")
out = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab Evaluation\output.txt", "w")

def dijkstra(src, u, graph, vis, dist):
    dist[u] = 0
    pq = []
    heapq.heappush(pq, (u, dist[u]))
    while pq:

        x, w = heapq.heappop(pq)
        if vis[x]:
            continue
        vis[x] = True
        for v in graph[x]:
            alt = dist[x] + v[1]
            if alt < dist[v[0]]:
                dist[v[0]] = alt
                heapq.heappush(pq, (v[0], dist[v[0]]))


n, m, k = list(map(int, inp.readline().split()))
graph = {}

for i in range(n):
    s, d, w = list(map(int, inp.readline().split()))

    if s not in graph:
        graph[s] = [(d, w)]
    else:
        graph[s].append( (d, w) )
dist = {}
dist[1] = 0
for j in range(k):
    s, w = list(map(int, inp.readline().split()))
    dist[s] = w

vis = {}
for i in graph.keys():
    vis[i] = False

print(graph)
for t in graph.keys():
    if t not in dist:
        dijkstra(1, t, graph, vis,  dist)
        # out.write()
print(dist)
print(len(graph))



inp.close()
out.close()