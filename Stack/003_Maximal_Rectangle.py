# 🔍 Problem: https://leetcode.com/problems/maximal-rectangle/
# 🔢 Difficulty: Hard
# ⏱️ Runtime: 31 ms


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        max_area = 0
        cols = len(matrix[0])
        heights = [0] * cols

        def largestRectangleArea(heights):
            stack = []
            max_area = 0
            heights.append(0)
            for i, h in enumerate(heights):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
            heights.pop()
            return max_area

        for row in matrix:
            for i in range(cols):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            max_area = max(max_area, largestRectangleArea(heights))
        return max_area
