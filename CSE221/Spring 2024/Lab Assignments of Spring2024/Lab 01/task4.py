def bubbleSort(data, test):
    flag = True
    for i in range(test-1):
        for j in range(test-i-1):
            if data[j][0] > data[j+1][0]:
                data[j], data[j+1] = data[j+1], data[j]
                flag = True
            elif data[j][0] == data[i+1][0]:
                if data[j][len(data[j])-1] >  data[j+1][len(data[j+1])-1]:
                    data[j], data[j+1] = data[j+1], data[j]
        if not flag:
            break

inp = open("F:\Academic\CSE221\Lab Assignments of Spring2024\Lab 01\input4.txt", "r")
out = open("F:\Academic\CSE221\Lab Assignments of Spring2024\Lab 01\output4.txt", "w")

test = int(inp.readline())
data = []
for i in range(test):
    data.append(inp.readline().split())

bubbleSort(data, test)

for k in range(test):
    out.write(' '.join(data[k]))
    out.write('\n')

out.close()
inp.close()