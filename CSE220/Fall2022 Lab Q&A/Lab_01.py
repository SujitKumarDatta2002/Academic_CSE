# def shiftLeft(source, k):

#     for i in range(len(source)-k):
#         source[i] = source[i+k]
#         source[i+k] = 0

#     print(source)

# source = [10, 20, 30, 40, 50, 60]
# shiftLeft(source, 3)


# def rotateLeft(source, k):

#     for i in range(len(source)-k):
#         source[i], source[i+k] = source[i+k], source[i]

#     print(source)

# source = [10, 20, 30, 40, 50, 60]
# rotateLeft(source, 3)


# def shiftRight(source, k):

#     for i in range(len(source)-k):
#         source[i+k] = source[i]
#         source[i] = 0

#     print(source)

# source = [10, 20, 30, 40, 50, 60]
# shiftRight(source, 3)


# def rotateRight(source, k):

#     for i in range(len(source)-k):
#         source[i+k], source[i] = source[i], source[i+k]

#     print(source)

# source = [10, 20, 30, 40, 50, 60]
# rotateRight(source, 3)


# def remove(source, size, idx):

#     k = 0
#     for i in range(size):
#         if i == idx:
#             k += 1
#         else:
#             source[i-k] = source[i]
#     source[size-1] = 0
#     print(source)

# source = [10, 20, 30, 40, 50, 0, 0]
# remove(source, 5, 2)


# def removeAll(source, size, element):

#     k = 0
#     for i in range(size):
#         if element == source[i]:
#             k += 1
#         else:
#             source[i - k] = source[i]

#     for j in range(k-1, len(source)):
#         source[j] = 0

#     print(source)


# source = [10, 2, 30, 2, 50, 2, 2, 0, 0]
# removeAll(source, 7, 2)


# def spliittingArray(arr):

#     zero = [0]
#     empty = []
#     logic = None
#     for i in range(len(arr)):
#         if i == 0:
#             zero[i] = arr[i]
#             empty = arr[i+1:len(arr)]
#             if sum(zero) == sum(empty):
#                 logic = True
#                 break
#             else:
#                 zero = []
#                 logic = False
#         else:
#             zero = arr[0:i+1]
#             empty = arr[i+1: len(arr)]
#             if sum(zero) == sum(empty):
#                 logic = True
#                 break
#             else:
#                 logic = False
#     return logic


# source = [1, 1, 1, 2, 1]
# print(spliittingArray(source))


# def sqauredArray(n):

#     n_sq = (n*n)
#     newArray = [0]*n_sq
#     x = 0
#     while x <= n:

#         y = 1
#         while y <= x:
#             newArray[(x*n)-y] = y
#             y += 1

#         x += 1

#     return newArray


# n = int(input("Enter the value of n: "))
# print(sqauredArray(n))


# def bunchArray(source):

#     maxList = []
#     first = source[0]
#     count = 0
#     for i in source:
#         if i == first:
#             count += 1
#         else:
#             first = i
#             count = 1
#         maxList.append(count)

#     return max(maxList)


# source = [1, 2, 2, 3, 4, 4, 4]
# print(bunchArray(source))


def repetition(source):

    # newList = []
    # first = source[0]
    # count = 0
    # for i in source:
    #     if i == first:
    #         count += 1
    #     else:
    #         first = i
    #         count = 1
    #     newList.append(count)
    mydict = {}
    for i in source:
        if i not in mydict:
            mydict[i] = 1
        else:
            mydict[i] += 1

    total = []
    for j in mydict.values():
        if j > 1:
            total.append(j)
    if len(total) == len(set(total)):
        return False
    else:
        return True


source = [3, 4, 6, 3, 4, 7, 4, 6, 8, 6, 6]
print(repetition(source))
