def find_max(arr, start, end):
    if start == end:
        return arr[start]
    mid = (start + end) // 2
    max1 = find_max(arr, start, mid)
    max2 = find_max(arr, mid + 1, end)

    if max1 > max2:
        return max1
    else:
        return max2


f4i = open('input4.txt', 'r')
f4o = open('output4.txt', 'w')

total = int(f4i.readline())

arr = list(map(int, f4i.readline().split(' ')))
max_value = find_max(arr, 0, total - 1)
f4o.write(str(max_value))

f4i.close()
f4o.close()

# Time complexity O(nlogn).
