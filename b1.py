import string
def solution(param0):
    ans = [float('inf')]
    dic = cords()
    def helper(first, second, cost, text, i):
        if i == len(text):
            ans[0] = min(ans[0], cost)
            return

        if first == "None":
            helper(text[i], second, cost, text, i+1)
        else:
            cord1 = dic[first]
            cord2 = dic[text[i]]
            c = dist(cord1[0], cord1[1], cord2[0], cord2[1])
            helper(text[i], second, cost+c, text, i+1)

        if second == "None":
            helper(first, text[i], cost, text, i+1)
        else:
            cord1 = dic[second]
            cord2 = dic[text[i]]
            c = dist(cord1[0], cord1[1], cord2[0], cord2[1])
            helper(first, text[i], cost + c, text, i+1)
    helper("None", "None", 0, param0, 0)

    return ans[0]


def dist(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)

def cords():
    char_list = string.ascii_uppercase
    dic = {}
    x, y = 0, 0
    for ch in char_list:
        dic[ch] = [x, y]
        y += 1
        if y == 6:
            y=0
            x+=1
    return dic

print(solution("HAPPY"))
