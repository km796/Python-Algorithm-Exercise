def solution(paper, n):
    ans = [max(paper)]
    def helper(path, k):
        if k > n:
            return
        for i in range(len(path) - 1):
            npath = make(path, i+1)
            nm = max(npath)
            ans[0] = max(ans[0], nm)
            helper(npath, k+1)
    helper(paper, 1)
    return ans

def make(path, k):
    left = path[:k]
    right = path[k:]

    ans = []
    if len(left) >= len(right):
        for i in range(len(right)):
            left[-(i+1)] += right[i]
        return left
    else:
        j = 0
        for i in range(len(left)-1, -1, -1):
            right[j] += left[i]
            j += 1
        return right


# print(solution([7,3,5,-2,9], 2))
print(solution([2,2,2,2,2], 2))

