# 🔍 Problem: https://leetcode.com/problems/group-anagrams/
# 🔢 Difficulty: Medium
# ⏱️ Runtime: 12 ms


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key not in dictionary:
                dictionary[key] = []
            dictionary[key].append(i)
        return list(dictionary.values())