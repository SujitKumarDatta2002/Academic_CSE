flag = True
def trop_sort(n, graph, visited, trop_ord, rec_path):
  global flag
  if n not in rec_path:

    rec_path.append(n)
  else:
    flag = False
    return flag

  visited[n] = 'B'
  for i in graph[n]:
    if visited[i] == 'W' and flag == True:
      trop_sort(i, graph, visited, trop_ord, rec_path)
  x = rec_path.pop(len(rec_path)-1)
  trop_ord.append(n)


inp1 = open("input1.txt","r")
out1 = open("output1.txt","w")

line1 = inp1.readline().split(' ')

M = int(line1[0])
N = int(line1[1])
graph = {}
startline = inp1.readline().split(' ')
key = int(startline[0])
start = key
val = int(startline[1])
if key not in graph.keys():
    graph[key] = [val]

else:

    graph[key].append(int(val))
lst2 = inp1.readlines()

for i in lst2:
  x = i.split(' ')

  key = int(x[0])
  val = int(x[1])

  if key not in graph.keys():
    graph[key] = [val]

  else:
    graph[key].append(val)
  if val not in graph.keys():
    graph[val] = []
visited = {}

for i in graph.keys():
  visited[i] = 'W'
trop_ord = []
rec_path = []
for j in graph.keys():
  if visited[j] == 'W':
    trop_sort(j, graph, visited, trop_ord, rec_path)
rt_str = ''
for i in range(len(trop_ord),0,-1):
  rt_str += str(trop_ord[i-1]) + ' '

out1.write(rt_str)
inp1.close()
out1.close()
