inp = open('F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 07\input4_1.txt', 'r')
out = open('F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 07\output4_1.txt', 'w')



def minCoins(coins, target):

    table = [float('inf')] * (target + 1)
    table[0] = 0

    for c in coins:
        for i in range(c, target + 1):
            table[i] = min(table[i], table[i - c] + 1)

    if table[target] != float('inf'):
        return table[target]
    else:
        return -1



N, X = list(map(int, inp.readline().split()))

cList = list(map(int, inp.readline().split()))

coins = []

for i in cList:
    coins.append(i)



result = str(minCoins(coins, X))
out.write(result)

inp.close()
out.close()
