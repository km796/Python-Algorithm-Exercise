from pandas import *

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        T = [[0]*(len(p)+1) for _ in range(len(s)+1)]

        s = "0"+s
        p = "0"+p
        T[0][0] = True

        sym = ['.', '*']
        for i in range(0, len(T)):
            for j in range(0, len(T[0])):
                if i == 0 and j == 0:
                    continue
                if p[j] not in sym or p[j] == '.':
                    T[i][j] = T[i-1][j-1] if p[j] == s[i] or p[j] == '.' else False
                    continue
                if p[j] == '*':
                    if T[i][j-2]:
                        T[i][j] = True
                    else:
                        if p[j-1] == s[i]:
                            T[i][j] = T[i-1][j]
                        elif p[j-1] == '.':
                            T[i][j] = T[i-1][j]
                        else:
                            T[i][j] = False
        df = DataFrame(T)
        df.columns = list(p)
        df.index = list(s)
        print(df)
        return T[-1][-1]

# s ="aab"
# p = "c*a*b"

s = "aaabaaaababcbccbaab"
p = "c*c*.*c*a*..*c*"

sol = Solution()
print(sol.isMatch(s, p))
