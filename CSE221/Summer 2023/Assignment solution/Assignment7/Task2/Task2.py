f1 = open('input2.txt', 'r')
f2 = open('output2.txt', 'w')



l1 = f1.readline().split()
N = int(l1[0])
M = int(l1[1])

tasksd = {}
for i in range(1, M+1):
  tasksd[i] = []

tasks = f1.readlines()

tasksl = []
for i in range(len(tasks)):
  start = int(tasks[i].split()[0])

  end = int(tasks[i].split()[1])
  tasksl.append((start, end))


for i in range(len(tasksl)):


    min_idx = i
    for j in range(i+1, len(tasksl)):
        if tasksl[min_idx][1] > tasksl[j][1]:
            min_idx = j


    tasksl[i], tasksl[min_idx] = tasksl[min_idx], tasksl[i]



tasksd = {}
for i in range(1, M+1):
  tasksd[i] = []
intervals = {}

usedl = []
for i in range(len(tasksl)):
  if i < len(tasksd):
    for j in range(len(tasksd)):
      for f in range(1, j+1):
        if j >= 1 and tasksl[j][0] == tasksd[f][-1][1]:
          if tasksl[j] not in usedl:
            tasksd[f].append(tasksl[j])
            usedl.append(tasksl[j])
          if tasksl[j+1] not in usedl:
            tasksd[j+1].append(tasksl[j+1])
            usedl.append(tasksl[j+1])

      if len(tasksd[j+1]) == 0:
        if tasksl[j] not in usedl:
          tasksd[j+1].append(tasksl[j])
          usedl.append(tasksl[j])



  else:


      for k in range(1, len(tasksd)+1):
        intervals[k] = tasksl[i][0] - tasksd[k][len(tasksd[k])-1][1]

      pos = []
      for keys, vals in intervals.items():
        if vals>=0:
          pos.append((keys, vals))
      for k in range(len(pos)):
        min_idx = k
        for l in range(k+1, len(pos)):
          if pos[min_idx][1] > pos[l][1]:
            min_idx = l


        pos[k], pos[min_idx] = pos[min_idx], pos[k]
      if len(pos)!=0:
        if tasksl[i] not in usedl:
          tasksd[pos[0][0]].append(tasksl[i])
          usedl.append(tasksl[i])

rt = 0
for k in tasksd:
  for l in tasksd[k]:
    rt+=1
f2.write(str(rt))
f1.close()
f2.close()
