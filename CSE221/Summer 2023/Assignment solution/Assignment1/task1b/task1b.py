fi1b = open('input1b.txt', 'r')
fo1b = open('output1b.txt', 'w')

num = fi1b.readline()

for line in range(int(num)):
  s = fi1b.readline()
  s1 = s.split(' ')
  fnum = int(s1[1])
  lnum = int(s1[3])
  op = s1[2]

  if op == '+':
    fo1b.write(f'The result of {fnum} + {lnum} is {str(fnum + lnum)}\n')
  if op == '-':
    fo1b.write(f'The result of {fnum} - {lnum} is {str(fnum - lnum)}\n')
  if op == '*':
    fo1b.write(f'The result of {fnum} * {lnum} is {str(fnum * lnum)}\n')
  if op == '/':
    fo1b.write(f'The result of {fnum} / {lnum} is {str(fnum / lnum)}\n')
fi1b.close()
fo1b.close()
