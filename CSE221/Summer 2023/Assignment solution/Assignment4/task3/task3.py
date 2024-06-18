def colourInitializing(G, ver_color):
  for i in G.keys():

    if i not in ver_color.keys():
      ver_color[i] = 0
    for j in G[i]:

      if str(j) not in ver_color.keys():
        ver_color[str(j)] = 0

def DFS(G,u, ver_color, retl):

  ver_color[str(u)] = 1
  retl.append(str(u))
  if str(u) in G.keys():
    for v in G[str(u)]:
      if ver_color[str(v)] == 0:

        DFS(G,v, ver_color, retl)





inp = open('input3.txt', 'r')
out = open('output3.txt', 'w')

line1 = inp.readline()
N, M= int(line1.split(' ')[0]), int(line1.split(' ')[1])

graph = {}


gline = inp.readline().split(' ')
start = gline[0]
if gline[0] not in graph.keys():
    graph[(gline[0])] = []
    graph[(gline[0])].append(int(gline[1]))
else:
    graph[(gline[0])].append(int(gline[1]))

for i in range(M-1):
  gline = inp.readline().split(' ')
  if gline[0] not in graph.keys():
    graph[(gline[0])] = []
    graph[(gline[0])].append(int(gline[1]))
  else:
    graph[(gline[0])].append(int(gline[1]))



ver_color = {}
colourInitializing(graph, ver_color)
retl = []
DFS(graph, start, ver_color, retl)
out_str = ''
for i in retl:
  out_str += str(i) + ' '
out.write(out_str)
inp.close()
out.close()
