inp = open("F:\Academic\CSE221\Lab Assignments of Spring2024\Lab 02\input2.txt", "r")
out = open("F:\Academic\CSE221\Lab Assignments of Spring2024\Lab 02\output2.txt", "w")


# O(nlogn)  solution using merge sort algorithm
def mergeSort(arr):

  if len(arr) == 1:
    return arr

  mid = len(arr) // 2

  l = mergeSort(arr[0:mid])
  r = mergeSort(arr[mid:len(arr)])

  return merge(l, r)

def merge(l1, l2):
  res = []
  i = 0
  j = 0
  while i<=len(l1)-1 and j<=len(l2)-1:
    if l1[i] <= l2[j]:
      res.append(l1[i])
      i += 1
    elif l2[j] < l1[i]:
      res.append(l2[j])
      j += 1
    if i == len(l1) or j == len(l2):
      break
  while i<len(l1):
    res.append(l1[i])
    i += 1
  while j<len(l2):
    res.append(l2[j])
    j += 1
  return res

# O(n) solution
def merge(l1, l2):
  res = []
  i = 0
  j = 0
  while i<=len(l1)-1 and j<=len(l2)-1:
    if l1[i] <= l2[j]:
      res.append(l1[i])
      i += 1
    elif l2[j] < l1[i]:
      res.append(l2[j])
      j += 1
    if i == len(l1) or j == len(l2):
      break
  while i<len(l1):
    res.append(l1[i])
    i += 1
  while j<len(l2):
    res.append(l2[j])
    j += 1
  return res

# input 1
N =  int(inp.readline())
n_arr = list(map(int,  inp.readline().split()))
M = int(inp.readline())
m_arr = list(map(int,  inp.readline().split()))
ret = list(map(str, merge(n_arr, m_arr)))
# result = list(map(str, mergeSort(n_arr+m_arr)))
out.write("Output 1 \n")
out.write(" ".join(ret) + "\n")

# input 2
N =  int(inp.readline())
n_arr = list(map(int,  inp.readline().split()))
M = int(inp.readline())
m_arr = list(map(int,  inp.readline().split()))
ret = list(map(str, merge(n_arr, m_arr)))
# result = list(map(str, mergeSort(n_arr+m_arr)))
out.write("Output 2 \n")
out.write(" ".join(ret) + "\n")

# input 3
N =  int(inp.readline())
n_arr = list(map(int,  inp.readline().split()))
M = int(inp.readline())
m_arr = list(map(int,  inp.readline().split()))
ret = list(map(str, merge(n_arr, m_arr)))
# result = list(map(str, mergeSort(n_arr+m_arr)))
out.write("Output 3 \n")
out.write(" ".join(ret) + "\n")

# input 4
N =  int(inp.readline())
n_arr = list(map(int,  inp.readline().split()))
M = int(inp.readline())
m_arr = list(map(int,  inp.readline().split()))
ret = list(map(str, merge(n_arr, m_arr)))
# result = list(map(str, mergeSort(n_arr+m_arr)))
out.write("Output 4 \n")
out.write(" ".join(ret) + "\n")


out.close()
inp.close()