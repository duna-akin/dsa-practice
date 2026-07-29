class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            currArea = min(heights[left], heights[right]) * (right - left)

            if currArea > maxArea:
                maxArea = currArea

            else:

                if heights[left] < heights[right]:
                    left += 1

                else:
                    right -= 1


        return maxArea





# Area = (min(heights[left], heights[right]) * (right - left))