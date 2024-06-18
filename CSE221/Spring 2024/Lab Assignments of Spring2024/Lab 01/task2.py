def bubbleSort(arr):
  flag = True
  for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        flag = True
    if not flag:
      break


inp = open("F:\Academic\CSE221\Lab Assignments of Spring2024\Lab 01\input2.txt", "r")
out = open("F:\Academic\CSE221\Lab Assignments of Spring2024\Lab 01\output2.txt", "w")

test = int(inp.readline())
arr = list(map(int, inp.readline().split()))
bubbleSort(arr)
res = " ".join(list(map(str, arr)))
out.write(res+"\n")


test2 = int(inp.readline())
arr2 = list(map(int, inp.readline().split()))
bubbleSort(arr)
res2 = " ".join(list(map(str, arr2)))
out.write(res2)

out.close()
inp.close()