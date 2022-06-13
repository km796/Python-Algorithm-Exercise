
def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return low-1
# def getMaxBarrier(initialEnergy, th):
#     initialEnergy.sort()
#     b = 0
#     while True:
#         k = binarySearch(initialEnergy, b, 0, len(initialEnergy)-1)
#         if k == -1:
#             s = sum(initialEnergy) - b*len(initialEnergy)
#         else:
#             s = sum(initialEnergy[k+1:])  - b*len(initialEnergy[k+1:])
#
#         if s>=th:
#             b+=1
#         else:
#             break
#
#     return b-1
# print(getMaxBarrier([5,2,13,10], 8))

def getMaxBarrier(initialEnergy, th):
    initialEnergy.sort()
    l = len(initialEnergy)
    SU = sum(initialEnergy)
    b = max(initialEnergy)
    while True:
        k = binarySearch(initialEnergy, b, 0, len(initialEnergy)-1)
        if k == -1:
            s = sum(initialEnergy) - b*len(initialEnergy)
        else:
            s = sum(initialEnergy[k+1:])  - b*len(initialEnergy[k+1:])

        if s>=th:
            return b
        else:
            b -= 1
        if b < 0:
            return 0

    return b-1


print(getMaxBarrier([15,7,8,19,8], 1))



# t = [1,2,3,5,10,19,20]
# print(binarySearch([1,2,3,5,10,19,20], 0, 0, len(t)-1))
