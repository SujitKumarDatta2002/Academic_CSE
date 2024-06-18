inp = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 03\input2.txt", "r")
out = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 03\output2.txt", "w")

def search(arr, max = 0):
    if len(arr) == 1:
        return arr[0]
    max = arr[0]
    mid = len(arr)//2
    l = search(arr[0:mid], max)
    r = search(arr[mid:len(arr)], max)
    return checker(l, r)

def checker(a, b):
    if a>=b:
        return a
    return b

# Time complexity of my code is O(nlogn)
# Input 01
test = inp.readline()
arr = list(map(int, inp.readline().split()))
ret = search(arr)
out.write(f"Output 1\n{ret}\n")

# Input 02
test = inp.readline()
arr = list(map(int, inp.readline().split()))
ret = search(arr)
out.write(f"Output 1\n{ret}\n")

# Input 03
test = inp.readline()
arr = list(map(int, inp.readline().split()))
ret = search(arr)
out.write(f"Output 1\n{ret}\n")

# Input 04
test = inp.readline()
arr = list(map(int, inp.readline().split()))
ret = search(arr)
out.write(f"Output 1\n{ret}\n")