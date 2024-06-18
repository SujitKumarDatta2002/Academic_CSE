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


inp = open("F:\Academic\CSE221\Lab Assignments of Spring2024\Lab 01\input3.txt", "r")
out = open("F:\Academic\CSE221\Lab Assignments of Spring2024\Lab 01\output3.txt", "w")


# Input 1
out.write("Output 1\n")
test = int(inp.readline())
arr = list(map(int, inp.readline().split()))
arr2 = list(map(int, inp.readline().split()))
selectionSort(arr, arr2)
for i in range(test-1, -1, -1):
    result = f"ID: {arr[i]} Mark: {arr2[i]}\n"
    out.write(result)

# Input 2
out.write("Output 2\n")
test2 = int(inp.readline())
arr3 = list(map(int, inp.readline().split()))
arr4 = list(map(int, inp.readline().split()))
selectionSort(arr3, arr4)
for i in range(test2-1, -1, -1):
    result = f"ID: {arr3[i]} Mark: {arr4[i]}\n"
    out.write(result)


out.close()
inp.close()