
temp = format(1000, "b")

print(temp)

def solution(s, n):

    for i in range(1, n+1):
        temp = format(i, "b")
        if temp not in s:
            return False

    return True

print(solution("0110", 1000))
