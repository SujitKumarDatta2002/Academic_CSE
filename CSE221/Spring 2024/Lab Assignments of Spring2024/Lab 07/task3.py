
inp = open('F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 07\input3_4.txt', 'r')
out = open('F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 07\output3_4.txt', 'w')


def findWays(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        arr = [0]*(num+1)
        arr[1] = 1
        arr[2] = 2
        for i in range(3, num + 1):
            arr[i] = arr[i - 1] + arr[i - 2]
        return arr[num]


N = int(inp.readline())
x = findWays(N)

out.write(str(x))

inp.close()
out.close()