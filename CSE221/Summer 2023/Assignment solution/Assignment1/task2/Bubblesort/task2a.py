def bubbleSort(arr):
  for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]

fi2 = open('input1.txt', 'r')
fo2 = open('output1.txt', 'w')

num = int(fi2.readline())

numlst = fi2.readline().split(' ')
numlist2 = [0]*num
for i in range(num):
  numlist2[i] = int(numlst[i])
bubbleSort(numlist2)
writestr = ''
for j in numlist2:
  writestr += str(j) + ' '

fo2.write(writestr)

fi2.close()
fo2.close()