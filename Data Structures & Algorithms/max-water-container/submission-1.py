class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        # start with the max possible width
        left = 0
        right = len(heights) - 1

        while left < right:
            # calculate current area
            currArea = (right - left) * min(heights[left], heights[right])

            if currArea > maxArea:
                maxArea = currArea

            # check which is the bottleneck
            else:
                if heights[left] < heights[right]:
                    left += 1
                else:
                    right -= 1

        return maxArea
                
