inp2 = open("input1b.txt","r")
out2 = open("output1b.txt","w")

line1 = inp2.readline().split(' ')
M = int(line1[0])
N = int(line1[1])
graph1 = {}

lst = inp2.readlines()

for i in lst:
  x = i.split(' ')

  key = int(x[0])
  val = [(int(x[1]),int(x[2]))]

  if key not in graph1.keys():
    graph1[key] = val
  else:
    graph1[key] += val



res_str = ""
for i in range(M+1):
  res_str += f"{i}:"
  if i in graph1:
    for z in graph1[i]:
      res_str += str(z)
  res_str+= "\n"
out2.write(res_str)
inp2.close()
out2.close()
