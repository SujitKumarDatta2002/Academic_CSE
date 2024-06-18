def merge(a, b):

  n1 = len(a)
  n2 = len(b)
  n = n1+n2
  c = [0]*n
  i = 0
  j = 0
  k = 0
  while i < n1 and j < n2:
    if a[i]<b[j]:
      c[k] = a[i]
      i += 1
    else:
      c[k] = b[j]
      j += 1
    k += 1
  if i == n1 and j != n2:
    c[k:] = b[j:]
  elif j == n2 and i != n1:
    c[k:] = a[i:]
  return c


def mergeSort(arr):
  if len(arr) <= 1:
    return arr
  else:
    mid = len(arr)//2
    a1 = mergeSort(arr[:mid])
    a2 = mergeSort(arr[mid:])
    return merge(a1, a2)

f3 = open('input3.txt', 'r')
o3 = open('output3.txt', 'w')

cnt = f3.readline()
cnt = int(cnt)

numarr = f3.readline().split(' ')
numarr1 = [0]*cnt
for i in range(cnt):
  numarr1[i] = int(numarr[i])
addarr = mergeSort(numarr1)
addstr = ''
for nums in addarr:
  addstr += str(nums)
  addstr += ' '
o3.write(addstr)

f3.close()
o3.close()
