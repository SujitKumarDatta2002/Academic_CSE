inp = open("F:\Academic\CSE221\Lab Assignments of Spring2024\Lab 02\input3.txt", "r")
out = open("F:\Academic\CSE221\Lab Assignments of Spring2024\Lab 02\output3.txt", "w")


def selectionSort(arr, arr2):
    for i in range(len(arr2)):
        last = len(arr2) - i - 1
        max = 0
        for j in range(last+1):
            if arr2[j] > arr2[max]:
                max = j
        temp2 = arr2[last]
        arr2[last] = arr2[max]
        arr2[max] = temp2

        temp = arr[last]
        arr[last] = arr[max]
        arr[max] = temp


# input 1
test = int(inp.readline())
work = [(0, 0)]
temps = []
tempe = []
while test > 0:
    start, end = list(map(int,  inp.readline().split()))    
    temps.append(start)
    tempe.append(end)
    test -= 1
selectionSort(temps, tempe)
for i in range(len(temps)):
    st, en = temps[i], tempe[i]
    if work[-1][1] <= en and work[-1][1] <= st:
        work.append((st, en))

out.write("Output 1 \n")
out.write(str(len(work)-1) + "\n")
for k in range(1,len(work)):
    out.write(str(work[k][0])+" "+ str(work[k][1]) +"\n")

# input 2
test = int(inp.readline())

work = [(0, 0)]
temps = []
tempe = []
while test > 0:
    start, end = list(map(int,  inp.readline().split()))    
    temps.append(start)
    tempe.append(end)
    test -= 1
selectionSort(temps, tempe)
for i in range(len(temps)):
    st, en = temps[i], tempe[i]
    if work[-1][1] <= en and work[-1][1] <= st:
        work.append((st, en))

out.write("Output 2 \n")
out.write(str(len(work)-1) + "\n")
for k in range(1,len(work)):
    out.write(str(work[k][0])+" "+ str(work[k][1]) +"\n")


# input 3
test = int(inp.readline())

work = [(0, 0)]
temps = []
tempe = []
while test > 0:
    start, end = list(map(int,  inp.readline().split()))    
    temps.append(start)
    tempe.append(end)
    test -= 1
selectionSort(temps, tempe)
for i in range(len(temps)):
    st, en = temps[i], tempe[i]
    if work[-1][1] <= en and work[-1][1] <= st:
        work.append((st, en))

out.write("Output 3 \n")
out.write(str(len(work)-1) + "\n")
for k in range(1,len(work)):
    out.write(str(work[k][0])+" "+ str(work[k][1]) +"\n")

inp.close()
out.close()