inp = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 04\input1A.txt", "r")
out = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 04\output1A.txt", "w")


def graphRepresentation(v, e):

  mat = []
  for i in range(v+1):
    row = [0]*(v+1)
    mat.append(row)

  for i in range(e):
    src, dest, cost = list(map(int, inp.readline().split()))
    mat[src][dest] = cost

  return mat

# Input 01
v,e = list(map(int, inp.readline().split()))
res = graphRepresentation(v, e)
out.write("Output 1\n")
for j in range(v+1):
  out.write(" ".join(list(map(str, res[j]))) + "\n")


# Input 02
v,e = list(map(int, inp.readline().split()))
res = graphRepresentation(v, e)
out.write("Output 2\n")
for j in range(v+1):
  out.write(" ".join(list(map(str, res[j]))) + "\n")

inp.close()
out.close()