class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxStreak = 0

        for n in numSet:
            if (n - 1) not in numSet:
                curStreak = 0
                while (n + curStreak) in numSet:
                    curStreak += 1
                maxStreak = max(curStreak, maxStreak)

        return maxStreak