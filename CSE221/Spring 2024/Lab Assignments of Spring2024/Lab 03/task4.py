inp = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 03\input4.txt", "r")
out = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 03\output4.txt", "w")


def findSum(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr)//2
    l = findSum(arr[0:mid])
    r = findSum(arr[mid:len(arr)])
    return  helper(l,r)

def helper(l , r):
    global total 
    result = []
    i = 0
    j = 0
    count1 = max(l) + (max(r))**2
    count2 = abs(max(l)) + abs(min(r))**2
    total = max(total, count1, count2)
    while i<len(l):
        result.append(l[i])
        i += 1
    while j<len(r):
        result.append(r[j])
        j += 1
    return result

# Input 01
total = 0
test = int(inp.readline())
arr = list(map(int, inp.readline().split()))
call = findSum(arr)

out.write("Output 01\n"+str(total)+"\n")

# Input 02
total = 0
test = int(inp.readline())
arr = list(map(int, inp.readline().split()))
call = findSum(arr)

out.write("Output 02\n"+str(total)+"\n")

# Input 03
total = 0
test = int(inp.readline())
arr = list(map(int, inp.readline().split()))
call = findSum(arr)

out.write("Output 03\n"+str(total)+"\n")

inp.close()
out.close()