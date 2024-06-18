def bfs(graph, start, queue):
    queue = [(start, 0)]

    visited = set()
    farthest_node = None
    max_distance = 0

    while queue:
        u, distance = queue.pop(0)

        visited.add(u)

        if distance > max_distance:
            max_distance = distance
            farthest_node = u

        for v in graph[u]:
            if v not in visited:
                queue.append((v, distance + 1))

    return farthest_node

inp7 = open("input7.txt","r")
out7 = open("output7.txt","w")

line1 = inp7.readline()

R = int(line1)


graph = {}

for i in range(R):
  graph[i+1] = []

line2 = inp7.readline().split(' ')
u = int(line2[0])
v = int(line2[1])
graph[u].append(v)
graph[v].append(u)
start = u
for _ in range(R-2):

        line = inp7.readline().split(' ')
        u = int(line[0])
        v = int(line[1])
        graph[u].append(v)
        graph[v].append(u)

queue = []

farthest_from_start = bfs(graph, start, queue)


farthest_from_farthest = bfs(graph, farthest_from_start, queue)

out7.write(f'{farthest_from_start} {farthest_from_farthest}')


inp7.close()
out7.close()