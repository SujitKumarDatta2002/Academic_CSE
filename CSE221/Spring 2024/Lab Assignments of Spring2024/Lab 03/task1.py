inp = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 03\input1.txt", "r")
out = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 03\output1.txt", "w")


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[0:mid]) # write the parameter
        a2 = mergeSort(arr[mid:len(arr)]) # write the parameter
    return merge(a1, a2) 

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

# Input 01
test = inp.readline()
arr = list(map(int, inp.readline().split()))
ret = mergeSort(arr)
out.write(' '.join([str(x) for x in ret]) + "\n")

# Input 02
test = inp.readline()
arr = list(map(int, inp.readline().split()))
ret = mergeSort(arr)
out.write(' '.join([str(x) for x in ret]) + "\n")

# Input 03
test = inp.readline()
arr = list(map(int, inp.readline().split()))
ret = mergeSort(arr)
out.write(' '.join([str(x) for x in ret]) + "\n")

# Input 04
test = inp.readline()
arr = list(map(int, inp.readline().split()))
ret = mergeSort(arr)
out.write(' '.join([str(x) for x in ret]) + "\n")



inp.close()
out.close()