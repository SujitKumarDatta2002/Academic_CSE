inp1 = open('input1.txt', 'r')
out1 = open('output1.txt', 'w')


l1 = inp1.readline()
N = int(l1)


tasks = inp1.readlines()

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



assigned = []
for i in range(len(tasksl)):
  if i == 0:
    assigned.append(tasksl[i])
  else:
    if tasksl[i][0] >= assigned[-1][1]:
      assigned.append(tasksl[i])

out1.write(str(len(assigned)))
for i in assigned:
  out1.write(f'\n{i[0]} {i[1]}')
inp1.close()
out1.close()
