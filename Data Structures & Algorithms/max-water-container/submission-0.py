class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        for left in range(len(heights)):
            for right in range(left + 1, len(heights)):
                currArea = (right - left) * min(heights[left], heights[right])
                
                if currArea > maxArea:
                    maxArea = currArea

        return maxArea
                
