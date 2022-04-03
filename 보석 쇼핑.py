from collections import Counter
def solution(gems):

    counter = Counter(gems)
    unique = len(counter.keys())
    length = len(gems)
    left = 0
    right = 0
    flag = False
    li = []
    dic = {}
    dic[gems[left]] = 1
    min = float('inf')
    cand = []

    while right < length:
        l = gems[left]
        r = gems[right]
        if len(dic) == unique and min > right - left:
            cand = ([left, right])
            min = right - left

        if dic[l] > 1:
            left += 1
            dic[l] -= 1
        else:
            right += 1
            if right<length:
                dic.setdefault(gems[right], 0)
                dic[gems[right]] += 1

    return [cand[0]+1, cand[1]+1]




gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))

# from collections import Counter
# def solution(gems):
#
#     counter = Counter(gems)
#     unique = len(counter.keys())
#     left = 0
#     right = len(gems) - 1
#
#     while left < right:
#         l = gems[left]
#         r = gems[right]
#
#         if counter[r] > 1:
#             right -= 1
#             counter[r] -= 1
#             continue
#         elif counter[l] > 1:
#             left += 1
#             counter[l] -= 1
#         else:
#             break
#     return [left+1, right+1]
#
# gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# print(solution(gems))


# from collections import Counter
# def solution(gems):
#     lr = leftRight(gems)
#     rl = rightLeft(gems)
#
#     if lr[1]-lr[0] < rl[1]-lr[0]:
#         return lr
#     else:
#         return rl
#
# def rightLeft(gems):
#     counter = Counter(gems)
#
#     left = 0
#     right = len(gems) - 1
#
#
#     while left < right:
#         r = gems[right]
#         if counter[r] <= 1:
#             break
#         counter[r] -= 1
#         right -= 1
#
#     while left < right:
#         l = gems[left]
#         if counter[l] <= 1:
#             break
#         counter[l] -= 1
#         left += 1
#
#     return [left+1, right+1]
#
# def leftRight(gems):
#     counter = Counter(gems)
#
#     left = 0
#     right = len(gems) - 1
#
#     while left < right:
#         l = gems[left]
#         if counter[l] <= 1:
#             break
#         counter[l] -= 1
#         left += 1
#     while left < right:
#         r = gems[right]
#         if counter[r] <= 1:
#             break
#         counter[r] -= 1
#         right -= 1
#     return [left+1, right+1]
