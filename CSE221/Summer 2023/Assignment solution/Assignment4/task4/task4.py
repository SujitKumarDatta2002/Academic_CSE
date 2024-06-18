flag = 'NO'
def dfs(start, graph3, color):
  global flag
  color[start] = 'G'

  for v in graph3[start]:
    if color[v] == 'W':

      dfs(v, graph3, color)
    elif color[v] == 'G':
      flag = 'YES'
  color[u] = 'B'
  return flag

inp4 = open("input4.txt","r")
out4 = open("output4.txt","w")

line1 = inp4.readline().split(' ')

M = int(line1[0])
N = int(line1[1])
graph3 = {}
startline = inp4.readline().split(' ')
key = startline[0]
start = key
val = startline[1]
if key not in graph3.keys():
    graph3[key] = list(str(int(val)))

else:

    graph3[key].append(str(int(val)))
lst2 = inp4.readlines()

for i in lst2:
  x = i.split(' ')

  key = (x[0])
  val = (x[1])

  if key not in graph3.keys():
    graph3[key] = list(str(int(val)))

  else:
    graph3[key].append(str(int(val)))
  if val not in graph3.keys():
    graph3[str(int(val))] = []


color = {}


for u in graph3.keys():
  color[u] = 'W'


st = dfs(start, graph3, color)
out4.write(st)
inp4.close()
out4.close()