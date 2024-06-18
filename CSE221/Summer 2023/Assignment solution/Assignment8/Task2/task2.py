def fib(num):
  arr = [0]*(num+1)
  if num == 1:
    arr[1] = 1
    return 1
  elif num == 2:
    arr[1] = 1
    arr[2] = 1
    return arr[1] + arr[2]
  else:
    arr[1] = 1
    arr[2] = 2
    for i in range(3, num + 1):
      arr[i] = arr[i - 1] + arr[i - 2]
    return arr[num]


f2 = open('input2.txt', 'r')
f3 = open('output2.txt', 'w')

N = int(f2.readline())
x = fib(N)
f3.write(str(x))

f2.close()
f3.close()