
inp = open('F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 07\input2_1.txt', 'r')
out = open('F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 07\output2_1.txt', 'w')


def findParent(parent, n):
    if parent[n] == n:
        return n
    else:
        return findParent(parent, parent[n])

def findingCost(parent, edge, i, j):
    pi = findParent(parent, i)
    pj = findParent(parent, j)

    if pi != pj:
        ci = 0
        cj = 0
        for k in parent.values():
            if k == pi:
                ci += 1
            elif k == pj:
                cj += 1
        if ci < cj:
                parent[i] = pj
        else:
                parent[j] = pi
        return edge
    return 0



N, M = list(map(int, inp.readline().split()))
graph = {}
for i in range(1, N+1):
    graph[i] = []
start = 0


edges = {}
weights = []
for i in range(M):
    s, d, w = list(map(int, inp.readline().split()))
    graph[s].append((d, w))
    
    if w not in edges.keys():
        edges[w] = [(s, d)]
        weights.append(w)
    else:
        edges[w] += [(s, d)]
        weights.append(w)

parent = {}
for i in range(1, N+1):
    parent[i] = i

weights.sort()

ew = {}
for i in weights:
    ew[i] = edges[i]


count = 0
for edge in ew:
    for nodes in ew[edge]:
        count += findingCost(parent, edge, nodes[0], nodes[1])

out.write(str(count))

inp.close()
out.close()
