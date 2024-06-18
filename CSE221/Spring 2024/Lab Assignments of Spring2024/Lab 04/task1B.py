inp = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 04\input1B.txt", "r")
out = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 04\output1B.txt", "w")


def graphAdjacency(v, e):
  dic = {}
  for i in range(v+1):
    dic[i] = []

  for j in range(e):
    src, dest, cost = list(map(int, inp.readline().split()))
    dic[src].append((dest, cost))
  return dic


# Input 01
v,e = list(map(int, inp.readline().split()))

res = graphAdjacency(v, e)
out.write("Output 1\n")
for k in range(v+1):
  out.write(str(k)+":"+ " ".join(list(map(str, res[k]))) + "\n")

# Input 02
v,e = list(map(int, inp.readline().split()))

res = graphAdjacency(v, e)
out.write("Output 2\n")
for k in range(v+1):
  out.write(str(k)+":"+ " ".join(list(map(str, res[k]))) + "\n")

# Input 03
v,e = list(map(int, inp.readline().split()))

res = graphAdjacency(v, e)
out.write("Output 3\n")
for k in range(v+1):
  out.write(str(k)+":"+ " ".join(list(map(str, res[k]))) + "\n")

inp.close()
out.close()