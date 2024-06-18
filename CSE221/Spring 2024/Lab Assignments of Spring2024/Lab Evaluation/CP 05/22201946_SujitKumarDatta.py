
inp = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab Evaluation\input.txt","r")
out = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab Evaluation\output.txt","w")

def topo(u, graph, vis, seq, f):
    vis[u] = True
    for e in graph[u]:
        # if vis[e] == True and vis[u] == True:
        #     return -1
        if vis[e]:
            continue

        else:
            topo(e, graph, vis, seq, u)
    seq.append(u)


n,d = list(map(int, inp.readline( ).split()))

graph = {}
crs = list(map(str, inp.readline().split()))

for i in crs:
    graph[i] = []

for i in range(d):
    s, t = list(map(str, inp.readline().split()))
    graph[s].append(t)
    if i == 0:
        root = s

vis = {}
for i in crs:
    vis[i] = False
seq = []
for j in graph.keys():
    if not vis[j]:
        ret = topo(j, graph, vis, seq, j)
        if ret == -1:
            out.write("NO DEGREE FOR YOU!\n")
            

seq.reverse()
out.write(" ".join(seq))

inp.close()
out.close()