fi1a = open('input1a.txt', 'r')
fo1a = open('output1a.txt', 'w')
num = fi1a.readline()
for nums in range(int(num)):
  elem = fi1a.readline()
  elem2 = int(elem)
  if (elem2)%2==0:
    fo1a.write(str(elem2) + ' is an even number\n')
  else:
    fo1a.write(str(elem2) + ' is an odd number\n')
fi1a.close()
fo1a.close()
