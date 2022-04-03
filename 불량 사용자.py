
from itertools import permutations
def solution(user_id, banned_id):
    answer = 0
    bannedSet = []

    userIdPermut = permutations(user_id, len(banned_id))

    for users in userIdPermut:
        if not check(users, banned_id):
            continue

        users = set(users)
        if users not in bannedSet:
            bannedSet.append(users)

    return len(bannedSet)

def check(users, bans):
    for i in range(len(users)):
        if len(users[i]) != len(bans[i]):
            return False

        for j in range(len(users[i])):
            if bans[i][j] == "*":
                continue
            if users[i][j] != bans[i][j]:
                return False

    return True


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

print(solution(user_id, banned_id))
