

def bfs(graph2, result, queue, start):
  result.append(start)
  queue.append(start)
  while len(queue) != 0:
    elm = queue.pop(0)
    #Print
    if elm in graph2.keys():
      for i in graph2[elm]:
        if i not in result:
          result.append(i)
          queue.append(i)




inp3 = open("input2.txt","r")
out3 = open("output2.txt","w")

line1 = inp3.readline().split(' ')

M = int(line1[0])
N = int(line1[1])
graph2 = {}
startline = inp3.readline().split(' ')
key = startline[0]
start = key
val = startline[1]
if key not in graph2.keys():
    graph2[key] = list(str(int(val)))

else:

    graph2[key].append(str(int(val)))
lst1 = inp3.readlines()

for i in lst1:
  x = i.split(' ')

  key = (x[0])
  val = (x[1])

  if key not in graph2.keys():
    graph2[key] = list(str(int(val)))

  else:

    graph2[key].append(str(int(val)))

result = []
queue = []


bfs(graph2, result, queue, start)
ret_str = ''
for i in result:
  ret_str += i
  ret_str += ' '
out3.write(ret_str)
inp3.close()
out3.close()