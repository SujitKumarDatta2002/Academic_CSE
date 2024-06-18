fi1 = open('input1.txt', 'r')
fo1 = open('output1.txt', 'w')
l1 = fi1.readline()
num = int(l1.split(' ')[0])
sum = int(l1.split(' ')[1])
l2s = fi1.readline().split(' ')
l2i = [0]*num
for i in range(num):
  l2i[i] = int(l2s[i])

#For O(n)

dict = {}
target = 0
pstr = ''
for idx in range(num):
  target = sum - (l2i[idx])
  if str(target) not in dict.keys():
    dict[str(l2i[idx])] = idx+1
  else:

    pstr += f'{dict[str(target)]} {idx+1}'
fo1.write(pstr)

fi1.close()
fo1.close()
