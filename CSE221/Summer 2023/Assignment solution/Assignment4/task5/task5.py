def bfs_shortest_path(graph, start, d):
    queue = [(start, [start])]

    visited = set()

    while queue:
        u, path = queue.pop(0)



        if u == d:

            return path

        visited.add(u)

        for v in graph[u]:
            if v not in visited:
                queue.append((v, path + [v]))

    return None



inp5 = open("input5.txt","r")
out5 = open("output5.txt","w")

line1 = inp5.readline().split(' ')

M = int(line1[0])
N = int(line1[1])
D = int(line1[2])
graph4 = {}
startline = inp5.readline().split(' ')
key = int(startline[0])
start = key
val = int(startline[1])
if key not in graph4.keys():
    graph4[key] = [val]

else:

    graph4[key].append(val)
if val not in graph4.keys():
    graph4[val] = [key]

else:

    graph4[val].append(key)
lst2 = inp5.readlines()

for i in lst2:
  x = i.split(' ')

  key = int(x[0])
  val = int(x[1])

  if key not in graph4.keys():
    graph4[key] = [val]

  else:
    graph4[key].append(val)
  if val not in graph4.keys():
    graph4[val] = [key]

  else:

    graph4[val].append(key)

shortest_path = bfs_shortest_path(graph4, start, D)
rt_str = ''
if shortest_path:
        time_taken = len(shortest_path) - 1
        rt_str = f"Time: {time_taken}\nShortest Path: "
        for i in shortest_path:
            rt_str += str(i) + ' '
out5.write(rt_str)



inp5.close()
out5.close()
