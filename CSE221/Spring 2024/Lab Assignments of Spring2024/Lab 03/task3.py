inp = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 03\input3.txt", "r")
out = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 03\output3.txt", "w")

def findPair(arr):
    global count
    if len(arr) == 1:
        return arr
    
    mid = len(arr)//2
    l = findPair(arr[0:mid])
    r = findPair(arr[mid:len(arr)])
    return  mergePairs(l,r)

def mergePairs(l , r):
    global count
    result = []
    i = 0
    j = 0
    
    while i <= len(l)-1 and j<= len(r)-1:
        if l[i] > r[j]:
            count += len(l)-i
            result.append(r[j])
            j += 1
        else:
            result.append(l[i])
            i += 1
    while i<len(l):
        result.append(l[i])
        i += 1
    while j<len(r):
        result.append(r[j])
        j += 1
    return result

count = 0
test = inp.readline()
arr = list(map(int, inp.readline().split()))
print(findPair(arr))
print(count)

count = 0
test = inp.readline()
arr = list(map(int, inp.readline().split()))
print(findPair(arr))
print(count)

count = 0
test = inp.readline()
arr = list(map(int, inp.readline().split()))
print(findPair(arr))
print(count)

inp.close()
out.close()