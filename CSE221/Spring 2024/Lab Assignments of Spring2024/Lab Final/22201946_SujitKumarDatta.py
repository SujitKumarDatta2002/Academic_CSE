import heapq

inp = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab Final\input.txt", "r")
out = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab Final\output.txt", "w")


def dijkstra(src, graph, vis, dist):
    dist[src] = 0
    pq = []
    heapq.heappush(pq, (src, dist[src]))

    while pq:
        v, d = heapq.heappop(pq)
        if vis[v]:
            continue
        vis[v] = True
        for u,w in graph[v]:
            alt = d + w
            if alt < dist[u]:
                dist[u] = alt
                heapq.heappush(pq, (u, dist[u]))


n, m = list(map(int, inp.readline().split()))

graph = {}
oneToOne = {}
for i in range(1, n+1):
    graph[i] = []
    oneToOne[i] = []

for j in range(m):
    src, dest, w = list(map(int, inp.readline().split()))
    graph[src].append((dest, w))
    graph[dest].append((src, w))
    oneToOne[src].append((dest, w))
y, z = list(map(int, inp.readline().split()))

x = int(inp.readline())

visy = {}
disty = {}
visz = {}
distz = {}
for i in graph.keys():
    if i not in visy:
        disty[i] = float("inf")
        visy[i] = False
        distz[i] = float("inf")
        visz[i] = False

out.write("Output A: \n")

for i in oneToOne.keys():
    res = f"{i}: "
    for j in oneToOne[i]:
        res += f"({i},{j[0]}) , "
    # res = res[:-2]
    res += "\n"
    out.write(res)
print(graph)

shorty = dijkstra(y, graph, visy, disty)
shortz = dijkstra(z, graph, visz, distz)

print(disty, distz)

out.write("Output B: \n")
out.write(str(disty[x]  + distz[x]) + "\n")


minDist = 0
vertex = x
for i in disty.keys():
    if ((disty[i] + distz[i]) < minDist) and i != y and i != z:
        minDist = disty[i] + distz[i]
        vertex = i


out.write("Output C: \n")
out.write(str(vertex) + "\n")

# resy = f"{y}-->"
# resz = f"{z}-->"
# pathy = graph[y]
# pathz = graph[z]

# while pathy != vertex:
#     for i in pathy:
#         if i[0] == vertex:
#             resy += str(i[0])
#             break
#         else:
#             resy += str(i[0])
#             pathy = i
# print(resy)


out.write("Output D: \n")






inp.close()
out.close()