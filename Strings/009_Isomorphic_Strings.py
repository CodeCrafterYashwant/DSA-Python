# 🔍 Problem: https://leetcode.com/problems/isomorphic-strings/
# 🔢 Difficulty: Medium
# ⏱️ Runtime: 7 ms


def isIsomorphic(self, s: str, t: str) -> bool:
        s_link = {}
        t_link =  {}
        if len(s) != len(t):
            return (False)
        else:
            for i in range(len(s)):
                k = s[i]
                j = t[i]
                if k in s_link:
                    if s_link[k] != j:
                        return(False)
                else:
                    s_link[k] = j
                if j in t_link:
                    if t_link[j] != k:
                        return(False)
                else:
                    t_link[j] = k
        return(True)