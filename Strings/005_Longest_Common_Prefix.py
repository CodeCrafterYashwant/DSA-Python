# 🔍 Problem: https://leetcode.com/problems/longest-common-prefix/
# 🔢 Difficulty: Easy
# ⏱️ Runtime: 0 ms


def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in strs:
            while not i.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix