fi1 = open('input1.txt', 'r')
fo1 = open('output1.txt', 'w')
l1 = fi1.readline()
num = int(l1.split(' ')[0])
sum = int(l1.split(' ')[1])
l2s = fi1.readline().split(' ')
l2i = [0]*num
for i in range(num):
  l2i[i] = int(l2s[i])


#For O(n**2)


for nums in range(num):
  for j in range(nums+1, num):
    if l2i[nums]+l2i[j] == sum:
      wstr = (str(nums+1) + ' ' + str(j+1))
      fo1.write(wstr)
fi1.close()
fo1.close()
