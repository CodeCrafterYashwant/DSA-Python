# 🔍 Problem: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# 🔢 Difficulty: Easy


# Method = 1
# ⏱️ Runtime: 0 ms
def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        return [candy + extraCandies >= maximum for candy in candies]


# Method = 2
# ⏱️ Runtime: 0 ms
def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        k = []
        for i in candies:
            r = i + extraCandies 
            k.append(r)
        maximum = max(candies)
        result = []
        for i in k:
            if i>= maximum:
                result.append(True)
            else:
                result.append(False)
        return result


# Method = 3
# ⏱️ Runtime: 0 ms
def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        result = []
        for candie in candies:
            if candie + extraCandies >= maximum:
                result.append(True)
            else:
                result.append(False)
        return result