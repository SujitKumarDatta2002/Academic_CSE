#Insertion sort
def Sort(num,array):

    for idx in range(1, num):
        key = array[idx]
        j = idx - 1


        while j >= 0 and key < array[j]:

            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

fi2 = open('input2.txt', 'r')
fo2 = open('output2.txt', 'w')

num = int(fi2.readline())

numlst = fi2.readline().split(' ')
numlist2 = [0]*num
for i in range(num):
  numlist2[i] = int(numlst[i])
Sort(num, numlist2)
writestr = ''
for j in numlist2:
  writestr += str(j) + ' '
print(writestr)
fo2.write(writestr)

fi2.close()
fo2.close()

#Here, istead of bubble sort, insertion sort is used. Because for the best case where the list is already sorted, the outer loop runs n times and the inner loops doesn't run. that is why its time complexity for best case senario
