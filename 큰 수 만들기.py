def solution(number, k):

    builder = ''
    tot = len(number) - k
    stack = []
    popped = 0
    if tot == 0:
        return ''

    for n in number:
        while stack and stack[-1] < n and popped<k:
            stack.pop()
            popped += 1
        stack.append(n)
    return ''.join(stack[:tot])


# 1231234
# 775841
#4177252841
number = "4177252841"
k = 1

print(solution(number, k))
