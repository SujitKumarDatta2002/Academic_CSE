def makeSet(parent, n):
  parent[n] = n

def findP(parent, n):
  if parent[n] == n:
    return n
  else:
    return findP(parent, parent[n])

def Union(friendlist, parent, i, j):
  parentI = findP(parent, i)
  parentJ = findP(parent, j)
  if i in friendlist:
    print('yes')
  if parentI != parentJ:
    parent[i] == parentJ
    if len(friendlist) == 0:
      friendlist.append(set([i, j]))
      return 2
    else:
      added = False
      for k in range(len(friendlist)):
        rmve = None
        if i in friendlist[k] or j in friendlist[k]:
          friendlist[k].add(i)
          friendlist[k].add(j)
          added = True
          for m in range(len(friendlist)):
            for n in friendlist[m]:
              for o in range(m+1, len(friendlist)):
                if n in friendlist[o]:

                  friendlist[k] = friendlist[m].union(friendlist[o])
                  rmve = friendlist[o]
          if rmve != None:
            friendlist.remove(rmve)
          return len(friendlist[k])
      if added == False:
          friendlist.append({i, j})
          return 2
f3 = open('input3.txt', 'r')
f4 = open('output3.txt', 'w')

l1 = f3.readline().split()
N = int(l1[0])
M = int(l1[1])
parent = [None]*(N+1)
for i in range(1,N+1):
  makeSet(parent, i)

friendlist = []
for i in range(1,M+1):
  line = f3.readline().split(' ')
  u = int(line[0])
  v = int(line[1])
  count = Union(friendlist, parent, u, v)
  #print(friendlist)
  #print(count)
  f4.write(str(count) + '\n')

f3.close()
f4.close()
