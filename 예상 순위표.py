def solution(n,a,b):
    answer = 1

    while True:
        if a%2 != 0:
            a+=1
        if b%2 != 0:
            b+=1
        if a == b:
            return answer
        a /= 2
        b /= 2
        answer += 1

    return answer

print(solution(8, 4, 7))
