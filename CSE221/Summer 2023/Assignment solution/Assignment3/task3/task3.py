def partition(arr, p, r):
    element = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= element:
            i += 1

            temp1 = arr[i]
            arr[i] = arr[j]
            arr[j] = temp1

    temp2 = arr[i + 1]
    arr[i + 1] = arr[r]
    arr[r] = temp2
    return i + 1


def quickSort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quickSort(arr, p, q - 1)
        quickSort(arr, q + 1, r)


inp = open('input3.txt', 'r')
otp = open('output3.txt', 'w')

num = inp.readline()
num = int(num)

numlist = inp.readline().split(' ')
numarr = [0] * num
for i in range(num):
    numarr[i] = int(numlist[i])
quickSort(numarr, 0, num - 1)
retstr = ''
for i in range(num):
    retstr += str(numarr[i])
    retstr += ' '
otp.write(retstr)

inp.close()
otp.close()
