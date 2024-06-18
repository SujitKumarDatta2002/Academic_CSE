def minCoins(coins, target):

    dp_table = [float('inf')] * (target + 1)
    dp_table[0] = 0

    for coin in coins:
        for i in range(coin, target + 1):
            dp_table[i] = min(dp_table[i], dp_table[i - coin] + 1)
    #print(dp_table)
    if dp_table[target] != float('inf'):
      return dp_table[target]
    else:
      return -1


f4 = open('input3.txt', 'r')
f5 = open('output3.txt', 'w')

line1 = f4.readline().split(' ')
line2 = f4.readline().split(' ')


N = int(line1[0])
X = int(line1[1])
coins = []

for i in line2:
  coins.append(int(i))



result = str(minCoins(coins, X))
f5.write(result)

f4.close()
f5.close()