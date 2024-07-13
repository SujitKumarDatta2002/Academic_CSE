inp = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 03\input5.txt", "r")
out = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 03\output5.txt", "w")


def quickSort(A, p, r):
    if p<r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)



def partition(A, p, r):

    # Taking Last elemet as pivot
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i  += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp2 = A[i+1]
    A[i+1] = A[r]
    A[r] = temp2
    return i + 1

    # Taking first Element as Pivot
    # x = A[p]
    # i = p+1
    # for j in range(p+1, r+1):
    #     if A[j] < x:
            
    #         temp = A[i]
    #         A[i] = A[j]
    #         A[j] = temp
    #         i  += 1
    # A[p], A[i-1] = A[i-1], A[p]
    # return i-1

    # Taking Mid element as pivot
    # mid = (p+r)//2
    # A[p], A[mid] = A[mid], A[p]
    # x = A[p]
    # i = p+1
    # for j in range(p+1, r+1):
    #     if A[j] < x:
            
    #         temp = A[i]
    #         A[i] = A[j]
    #         A[j] = temp
    #         i  += 1
    # A[p], A[i-1] = A[i-1], A[p]
    # return i-1

# Input 01
test = int(inp.readline())
arr = list(map(int, inp.readline().split()))
quickSort(arr, 0, len(arr)-1)
out.write("Output 01\n")
out.write(" ".join(map(str, arr))+"\n")
# Input 02
test = int(inp.readline())
arr = list(map(int, inp.readline().split()))
quickSort(arr, 0, len(arr)-1)
out.write("Output 02\n")
out.write(" ".join(map(str, arr))+"\n")
# Input 03
test = int(inp.readline())
arr = list(map(int, inp.readline().split()))
quickSort(arr, 0, len(arr)-1)
out.write("Output 03\n")
out.write(" ".join(map(str, arr))+"\n")
# Input 04
test = int(inp.readline())
arr = list(map(int, inp.readline().split()))
quickSort(arr, 0, len(arr)-1)
out.write("Output 04\n")
out.write(" ".join(map(str, arr))+"\n")

inp.close()
out.close()