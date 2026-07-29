class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right, minNum = 0, len(nums) - 1, nums[0]
        while left <= right:
            if nums[left] < nums[right]: 
                minNum = nums[left]
                break
            mid = (left + right) // 2
            minNum = min(minNum, nums[mid])
            if nums[left] > nums[mid]:
                right = mid
            else:
                left = mid + 1
        return minNum