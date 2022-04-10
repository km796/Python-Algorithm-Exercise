from collections import deque
def solution(begin, target, words):
    answer = 0
    visited = set()

    def findClose(word):
        res = []
        for w in words:
            if diffBy1(w, word):
                res.append(w)
                words.remove(w)
        return res

    q = deque()
    q.append(begin)

    if begin in words:
        words.remove(begin)
    while q:
        size = len(q)
        for i in range(size):
            cur = q.popleft()
            if cur == target:
                return answer
            q.extend(findClose(cur))
        answer += 1

    return 0



def diffBy1(w1, w2):
    if len(w1) != len(w2):
        return False
    count = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            count += 1
            if count > 1:
                return False
    if count == 1:
        return True
    else:
        return False

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin,target, words))
