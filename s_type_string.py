def solution(line1, line2):
    vs = [line2]
    i = 1
    l2 = len(line2)
    ans = 0
    while True:
        n_str = ""
        for j in range(l2-1):
            n_str += line2[j] + '*'*i
        n_str += line2[-1]
        if len(n_str) > len(line1):
            break
        vs.append(n_str)
        i += 1

    for v in vs:
        for i in range(len(line1) - len(v) + 1):
            print(line1[i:i+len(v)])
            if compare(line1[i:i+len(v)], v):
                ans += 1
    return ans


def compare(s1, s2):
    for i in range(len(s1)):
        if s2[i] == '*':
            continue
        if s1[i] != s2[i]:
            return False
    return True

print(solution("abacaba", "acb"))
