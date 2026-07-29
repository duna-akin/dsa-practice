class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        sortedNums = sorted(set(nums))

        maxStreak = 1
        curStreak = 1

        for i in range(1, len(sortedNums)):
            if sortedNums[i - 1] + 1 == sortedNums[i]:
                curStreak += 1
            
            else:
                if curStreak > maxStreak:
                    maxStreak = curStreak
                curStreak = 1
            
        if curStreak > maxStreak:
            maxStreak = curStreak

        return maxStreak
