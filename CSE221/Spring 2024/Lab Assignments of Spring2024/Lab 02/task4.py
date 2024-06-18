inp = open("F:\Academic\CSE221\Lab Assignments of Spring2024\Lab 02\input4.txt", "r")
out = open("F:\Academic\CSE221\Lab Assignments of Spring2024\Lab 02\output4.txt", "w")

def selectionSort(arr, arr2):
    for i in range(len(arr2)):
        last = len(arr2) - i - 1
        max = 0
        for j in range(last+1):
            if arr2[j] > arr2[max]:
                max = j
        temp2 = arr2[last]
        arr2[last] = arr2[max]
        arr2[max] = temp2

        temp = arr[last]
        arr[last] = arr[max]
        arr[max] = temp

def mergeSort(arr):

  if len(arr) == 1:
    return arr

  mid = len(arr) // 2

  l = mergeSort(arr[0:mid])
  r = mergeSort(arr[mid:len(arr)])

  return merge(l, r)

def merge(l1, l2):
  res = []
  i = 0
  j = 0
  while i<=len(l1)-1 and j<=len(l2)-1:
    if l1[i] <= l2[j]:
      res.append(l1[i])
      i += 1
    elif l2[j] < l1[i]:
      res.append(l2[j])
      j += 1
    if i == len(l1) or j == len(l2):
      break
  while i<len(l1):
    res.append(l1[i])
    i += 1
  while j<len(l2):
    res.append(l2[j])
    j += 1
  return res


def findPerson(tup, people):
    min = 1000
    found = None
    for p in people:
        if p[-1][-1] ==0 and p[-1][-1] == 0:
            found = p
            continue
        if p[-1][-1] <= tup[1] and p[-1][-1] <= tup[0]:
            if abs(p[-1][-1] - tup[-1]) <= min:
                min = abs(p[-1][-1] - tup[-1])
                found = p
    return found


# If I use selection sort then the time complexity will be O(n2). If I use merge sort than the complexity will be O(nlogn).
# input 1
test, person = list(map(int, inp.readline().split()))

people = []
for i in range(person):
    people.append([(0,0)])

temps = []
tempe = []
while test > 0:
    start, end = list(map(int,  inp.readline().split()))    
    temps.append(start)
    tempe.append(end)
    test -= 1
selectionSort(temps, tempe)

for i in range(len(temps)):
    st, en = temps[i], tempe[i]
    rt = findPerson((st, en), people)
    if rt != None:
        rt.append((st, en))

total = 0
for f in range(len(people)):
    total += len(people[f])

out.write("Output 1 \n")
out.write(str(total-person) + "\n")

# Input 2
test, person = list(map(int, inp.readline().split()))

people = []
for i in range(person):
    people.append([(0,0)])

temps = []
tempe = []
while test > 0:
    start, end = list(map(int,  inp.readline().split()))    
    temps.append(start)
    tempe.append(end)
    test -= 1
selectionSort(temps, tempe)

for i in range(len(temps)):
    st, en = temps[i], tempe[i]
    rt = findPerson((st, en), people)
    if rt != None:
        rt.append((st, en))

total = 0
for f in range(len(people)):
    total += len(people[f])

out.write("Output 2 \n")
out.write(str(total-person) + "\n")

# Input 3
test, person = list(map(int, inp.readline().split()))

people = []
for i in range(person):
    people.append([(0,0)])

temps = []
tempe = []
while test > 0:
    start, end = list(map(int,  inp.readline().split()))    
    temps.append(start)
    tempe.append(end)
    test -= 1
selectionSort(temps, tempe)

for i in range(len(temps)):
    st, en = temps[i], tempe[i]
    rt = findPerson((st, en), people)
    if rt != None:
        rt.append((st, en))

total = 0
for f in range(len(people)):
    total += len(people[f])

out.write("Output 3 \n")
out.write(str(total-person) + "\n")

# Input 4
test, person = list(map(int, inp.readline().split()))

people = []
for i in range(person):
    people.append([(0,0)])

temps = []
tempe = []
while test > 0:
    start, end = list(map(int,  inp.readline().split()))    
    temps.append(start)
    tempe.append(end)
    test -= 1
selectionSort(temps, tempe)

for i in range(len(temps)):
    st, en = temps[i], tempe[i]
    rt = findPerson((st, en), people)
    if rt != None:
        rt.append((st, en))

total = 0
for f in range(len(people)):
    total += len(people[f])

out.write("Output 4 \n")
out.write(str(total-person) + "\n")

# Input 5
test, person = list(map(int, inp.readline().split()))

people = []
for i in range(person):
    people.append([(0,0)])

temps = []
tempe = []
while test > 0:
    start, end = list(map(int,  inp.readline().split()))    
    temps.append(start)
    tempe.append(end)
    test -= 1
selectionSort(temps, tempe)

for i in range(len(temps)):
    st, en = temps[i], tempe[i]
    rt = findPerson((st, en), people)
    if rt != None:
        rt.append((st, en))

total = 0
for f in range(len(people)):
    total += len(people[f])

out.write("Output 5 \n")
out.write(str(total-person) + "\n")



inp.close()
out.close()