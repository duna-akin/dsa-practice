class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        setNums = set(nums)
        maxStreak = 0

        for n in setNums:
            if (n - 1) not in setNums:
                curStreak = 0
                while (n + curStreak) in setNums:
                    curStreak += 1
                
                maxStreak = max(maxStreak, curStreak)

        return maxStreak