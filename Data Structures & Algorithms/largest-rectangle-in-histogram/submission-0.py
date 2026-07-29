class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                oldIndex, oldHeight = stack.pop()
                maxArea = max(maxArea, oldHeight * (i - oldIndex))
                start = oldIndex
            stack.append((start, height))

        for i, height in stack:
            maxArea = max(maxArea, height * (len(heights) - i))

        return maxArea