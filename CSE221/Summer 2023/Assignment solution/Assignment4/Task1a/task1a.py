inp1 = open("input1a.txt","r")
out1 = open("output1a.txt","w")

line1 = inp1.readline().split(' ')

M = int(line1[0])
N = int(line1[1])

arr = [[0 for i in range(M+1)] for i in range(M+1)]

for i in range(N):
  nline = inp1.readline().split(' ')
  nlist = [0]*3

  for i in range(3):
    nlist[i] = int(nline[i])

  i = nlist[0]
  j = nlist[1]
  k = nlist[2]
  arr[i][j] = k

for i in range(M+1):
  for j in range(M+1):
    out1.write(f'{arr[i][j]} ')
  out1.write('\n')

inp1.close()
out1.close()
