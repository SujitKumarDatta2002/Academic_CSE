def find_pair(arr, mval, left, right):

  if left == right:

    if mval>arr[left]:
        
        return 1
    else:
      return 0
  mid = (left + right) // 2
  count1 = 0 + find_pair(arr, mval, left, mid)
  count2 = 0 + find_pair(arr, mval, mid + 1, right)
  return count1+count2


f1 = open('input1.txt', 'r')
f2 = open('output1.txt', 'w')

count = int(f1.readline())


thlist = f1.readline().split(' ')

hlist = [0]*count

for i in range(count):
  hlist[i] = int(thlist[i])

pairCount = 0
for j in range(count-1):
  pairCount += find_pair(hlist, hlist[j], j+1, count-1)
paircount = str(pairCount)
f2.write(paircount)

f1.close()
f2.close()
