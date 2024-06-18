inp = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 03\input6.txt", "r")
out = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 03\output6.txt", "w")

def kth_smallest(arr, l, r, K):

    pos = partition(arr, l, r)
    if (pos - l == K - 1):
        return arr[pos]
    if (pos - l > K - 1):
        return kth_smallest(arr, l, pos - 1, K)

    return kth_smallest(arr, pos + 1, r, K - pos + l - 1)


def partition(A, p, r):
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

test = int(inp.readline())
arr = list(map(int, inp.readline().split()))

num = int(inp.readline())
for i in range(num):
    qur = int(inp.readline())
    out.write(str(kth_smallest(arr, 0, len(arr)-1, qur))+"\n")


inp.close()
out.close()