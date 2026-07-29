class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
		    # hashing the index
        map = {nums[0]: 0}

				# target - nums[i] is the difference
        for i in range(1, len(nums)):
            if target - nums[i] in map:
                return [map[target - nums[i]] ,i]
                
            map[nums[i]] = i # map/remember index of current number