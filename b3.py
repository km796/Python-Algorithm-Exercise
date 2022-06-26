

def solution(arr):
    c = 0

    for i in range(len(arr)):
        t = arr[i]
        if t % 2 == 1:
            c += 1
        for j in range(i+1, len(arr)):
            t = t + arr[j]
            if t % 2 == 1:
                c += 1
    return c
arr = [1,3,5]

print(solution(arr))
