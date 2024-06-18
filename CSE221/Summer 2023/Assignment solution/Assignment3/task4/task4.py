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


def kth_smallest(arr, l, r, K):
    pos = partition(arr, l, r)

    if (pos - l == K - 1):
        return arr[pos]

    if (pos - l > K - 1):
        return kth_smallest(arr, l, pos - 1, K)

    return kth_smallest(arr, pos + 1, r, K - pos + l - 1)


fi = open('input4.txt', 'r')
fo = open('output4.txt', 'w')

enum = fi.readline()
enum = int(enum)
numl = fi.readline().split(' ')
numarr2 = [0] * enum
for i in range(1, enum + 1):
    numarr2[i - 1] = int(numl[i - 1])

otpn = fi.readline()
otpn = int(otpn)

for j in range(1, otpn + 1):
    k = fi.readline()
    k = int(k)

    fo.writelines(str(kth_smallest(numarr2, 0, enum - 1, k)) + '\n')
fi.close()
fo.close()