class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = 0
        maxRight = 0

        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        # nothing to the left of left-most and nothing to the right of right-most
        maxLeft[0] = 0
        maxRight[-1] = 0

        # maxLeft calculation
        for i in range(1, len(height)):
            # max height seen to the left is the taller of the previous bar or the previous max
            maxLeft[i] = max(height[i - 1], maxLeft[i - 1]) 

        # maxRight calculation
        for i in range(len(height) - 2, -1, -1):
            # max height seen to the right is the taller of the next bar or the next max
            maxRight[i] = max(height[i + 1], maxRight[i + 1])

        resultArea = 0

        for i in range(len(height)):
            indexArea = min(maxRight[i], maxLeft[i]) - height[i]
            if indexArea > 0:
                resultArea += indexArea

        return resultArea