inp = open('F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 07\input1_2.txt', 'r')
out = open('F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 07\output1_2.txt', 'w')


def findParent(parent, n):
    if parent[n] == n:
        return n
    else:
        return findParent(parent, parent[n])

def makingFriends(friendCirlce, parent, i, j):

    pi = findParent(parent, i)
    pj = findParent(parent, j)

    if pi != pj:
        parent[i] == pj
        if len(friendCirlce) == 0:
            friendCirlce.append(set([i, j]))
            return 2
        else:
            added = False

            for k in range(len(friendCirlce)):
                rmve = None
                if i in friendCirlce[k] or j in friendCirlce[k]:
                    friendCirlce[k].add(i)
                    friendCirlce[k].add(j)
                    added = True

                    for m in range(len(friendCirlce)):
                        for n in friendCirlce[m]:
                            for p in range(m+1, len(friendCirlce)):
                                if n in friendCirlce[p]:
                                    friendCirlce[k] = friendCirlce[m].union(friendCirlce[p])
                                    rmve = friendCirlce[p]

                    if rmve != None:
                        friendCirlce.remove(rmve)
                    return len(friendCirlce[k])
                
            if added == False:
                friendCirlce.append(set([i, j]))
                return 2
        

N, K = list(map(int, inp.readline().split()))
parent = [0]*(N+1)
for i in range(1,N+1):
    parent[i] = i

friendCirlce = []
for i in range(1,K+1):
    u, v = list(map(int, inp.readline().split()))
    count = makingFriends(friendCirlce, parent, u, v)
    out.write(str(count) + '\n')


inp.close()
out.close()
