inp = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab Evaluation\CP 02\input.txt", "r")
out = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab Evaluation\CP 02\output.txt", "w")


def k_th_largest(arr, l, h, qur):
    position = partition(arr, l, h)
    if position - l == qur:
        return  arr[position]
    elif position - l > qur:
        return  k_th_largest(arr, l, position - 1, qur)
        # return k_th_largest(arr, (position + 1), h, (qur - (position - l)))
    return k_th_largest(arr, position + 1, h, qur)


def partition(arr, p, r):
    pivot = arr[r]
    cur = p-1
    for j in range(p, r):
        if arr[j] >= pivot:
            cur += 1
            temp = arr[cur]
            arr[cur] = arr[j]
            arr[j] = temp
    temp2 = arr[cur+1]
    arr[cur+1] = arr[j+1]
    arr[j+1] = temp2
    return cur+1


size = int(inp.readline())

arr = list(map(int, inp.readline().split()))
n = int(inp.readline())

for i in range(n):
    qur = int(inp.readline())
    out.write(str(k_th_largest(arr, 0, len(arr)-1, qur)) + "\n")


inp.close()
out.close()

