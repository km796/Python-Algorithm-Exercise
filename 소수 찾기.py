def solution(numbers):
    combs = set()

    def helper(path, idx):
        if path:
            pathNum = int(path)
            if isprime(pathNum):
                combs.add(pathNum)

        for i in range(idx, len(numbers)):
            helper(path+numbers[i], idx+1)

    helper("", 0)

    return len(combs)


def isprime(num):
    if num==0:
        return False
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

print(solution("011"))
