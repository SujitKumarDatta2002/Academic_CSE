fi2 = open('input2.txt', 'r')
fo2 = open('output2.txt', 'w')

num1 = fi2.readline()
num1 = int(num1)
lst1 = fi2.readline().split(' ')
num2 = fi2.readline()
num2 = int(num2)
lst2 = fi2.readline().split(' ')

mlist = [0]*(num1+num2)

i1 = 0
i2 = 0

for idxs in range(num1+num2):
  if i1<num1:
    if i2<num2:
      if int(lst1[i1])<int(lst2[i2]):
        mlist[idxs] = int(lst1[i1])
        i1+=1
      else:
        mlist[idxs] = int(lst2[i2])
        i2+=1
    elif i2==num2:
      mlist[idxs] = int(lst1[i1])
      i1+=1
  elif i2==num1 and i2<num2:
    mlist[idxs] = int(lst2[i2])
    i2+=1

fi2.close()
fo2.close()
