inp = open("F:\Academic\CSE221\Lab Assignments of Spring2024\Lab 02\input1.txt", "r")
out = open("F:\Academic\CSE221\Lab Assignments of Spring2024\Lab 02\output1.txt", "w")

# O(n2) solution of this problem
def findTargetSum(arr, size):
    res = ''
    for i in range(size):
        for j in range(i+1, size):
            if  arr[i] + arr[j] == target:
                res = f"{i+1} {j+1}"
                break
    if res == '':
        out.write("Impossible")

    else:
        out.write(res)


# O(n) solution of this problem
def findTargetSum2(arr, size):
    mydict = {}
    for i in range(size):
        diff = target - arr[i]
        if target-diff in mydict:
            return f"{mydict[target-diff]} {i+1}"
        if  diff not in mydict:
            mydict[diff] = i+1
    return "IMPOSSIBLE"

# input 1
size, target = list(map(int, inp.readline().split()))
arr = list(map(int, inp.readline().split()))
# findTargetSum(arr, size)
result =  findTargetSum2(arr, size)
out.write("Output 1\n")
out.write(result + "\n")

# input 2
out.write("Output 2\n")
size, target = list(map(int, inp.readline().split()))
arr = list(map(int, inp.readline().split()))
# findTargetSum(arr, size)
result =  findTargetSum2(arr, size)
out.write(result + "\n")

# input 3
out.write("Output 3\n")
size, target = list(map(int, inp.readline().split()))
arr = list(map(int, inp.readline().split()))
# findTargetSum(arr, size)
result =  findTargetSum2(arr, size)
out.write(result + "\n")

# input 4
out.write("Output 4\n")
size, target = list(map(int, inp.readline().split()))
arr = list(map(int, inp.readline().split()))
# findTargetSum(arr, size)
result =  findTargetSum2(arr, size)
out.write(result + "\n")

out.close()
inp.close()