def insertionSort(count, array, array2):
    for step in range(1, count):
        key = array[step]
        key2 = array2[step]
        j = step - 1

        while j >= 0 and key > array[j]:
            array[j + 1] = array[j]
            array2[j + 1] = array2[j]
            j = j - 1
        array[j + 1] = key
        array2[j + 1] = key2


def checkID(numi, IDi, i):
    if numi[i] != numi[i + 1]:
        return
    else:
        if IDi[i] > IDi[i + 1]:
            temp1 = IDi[i]
            IDi[i] = IDi[i + 1]
            IDi[i + 1] = temp1
            checkID(numi, IDi, i - 1)


fi3a = open('input3.txt', 'r')
fo3a = open('output3.txt', 'w')

count3 = fi3a.readline()
# print(count3)
count3 = int(count3)
ID = fi3a.readline().split(' ')
IDi = [0] * count3
for i in range(count3):
    IDi[i] = int(ID[i])

num = fi3a.readline().split(' ')
numi = [0] * count3
for j in range(count3):
    numi[j] = int(num[j])

insertionSort(count3, numi, IDi)

l = 0
for i in range(count3 - 1):
    checkID(numi, IDi, i)

retstr = ''
for j in range(count3):
    retstr = f'ID: {IDi[j]} Mark: {numi[j]}\n'
    fo3a.write(retstr)

fi3a.close()
fo3a.close()
