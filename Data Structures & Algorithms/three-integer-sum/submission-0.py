class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        result = list()

        for i in range(len(sortedNums)):
            if i != 0 and sortedNums[i] == sortedNums[i-1]:
                continue

            left = i + 1
            right = len(sortedNums) - 1

            while left < right:
                if sortedNums[left] + sortedNums[right] + sortedNums[i] > 0:
                    right -= 1

                elif sortedNums[left] + sortedNums[right] + sortedNums[i] < 0:
                    left += 1

                else:
                    result.append([sortedNums[i], sortedNums[left], sortedNums[right]])

                    # check for other combinations
                    left += 1
                    right -= 1

                    # keep incrementing left if it is same 
                    while left < right and sortedNums[left] == sortedNums[left-1]:
                        left += 1

        return result
