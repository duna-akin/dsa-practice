class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyTable = {}

        for i in range(0, len(nums)):
            frequencyTable[nums[i]] = frequencyTable.get(nums[i], 0) + 1

        # SORT THE DICTIONARY HERE
        frequencyTable = dict(sorted(frequencyTable.items(), reverse=True, key=lambda item: item[1]))

        # return the k keys with the most frequency as a list
        resultList = list()
        for key, value in frequencyTable.items():
            resultList.append(key)
            k -= 1
            if k == 0:
                break

        return resultList