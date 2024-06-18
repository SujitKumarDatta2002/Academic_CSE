fi2 = open('input2.txt', 'r')
fo2 = open('output2.txt', 'w')

num1 = fi2.readline()
num1 = int(num1)
lst1 = fi2.readline().split(' ')
num2 = fi2.readline()
num2 = int(num2)
lst2 = fi2.readline().split(' ')

mlist = [0]*(num1+num2)

#For O(nlogn)
for idx in range(num1+num2):
  if idx<num1:
    mlist[idx] = int(lst1[idx])
  else:
    mlist[idx] = int(lst2[idx-num1])

mlist.sort()
wstrg = ''
for i in mlist:
  wstrg += str(i)
  wstrg += ' '
fo2.write(wstrg)
fi2.close()
fo2.close()
