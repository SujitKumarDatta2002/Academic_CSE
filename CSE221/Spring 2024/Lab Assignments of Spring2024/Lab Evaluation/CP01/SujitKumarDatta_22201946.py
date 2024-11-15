inp = open("F:\Academic\CSE221\Lab Assignments of Spring2024\Lab Evaluation\input.txt", "r")
out = open("F:\Academic\CSE221\Lab Assignments of Spring2024\Lab Evaluation\output.txt", "w")

def merge(a, b):
    result = []
    i = len(a)-1
    j = len(b)-1

    while i>=0 and j>=0:
        if a[i] >= b[j]:
            result.append(a[i])
            i -= 1
        if b[j] >= a[i]:
            result.append(b[j])
            j -= 1
        if i < 0 or j<0:
            break

    while i >= 0:
        result.append(a[i])
        i -= 1

    while j >= 0:
        result.append(b[j])
        j -= 1
    return result

test = int(inp.readline())
arr1 = list(map(int, inp.readline().split()))
test2 = int(inp.readline())
arr2 = list(map(int, inp.readline().split()))
ret = merge(arr1, arr2)

out.write(' '.join(map(str, ret)) + '\n')
test = int(inp.readline())
arr1 = list(map(int, inp.readline().split()))
test2 = int(inp.readline())
arr2 = list(map(int, inp.readline().split()))
ret = merge(arr1, arr2)

out.write(' '.join(map(str, ret)) + '\n')

inp.close()
out.close()