class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = dict() # num: frequency

        for num in nums:
            count[num] = count.get(num, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)] # list of lists with index of inner list indicating frequency of nubmers stored

        for num, frequency in count.items():
            freq[frequency].append(num)

        
        result = list()

        for i in range(len(freq) - 1, 0, -1): # no need to check 0 index
            for num in freq[i]:
                result.append(num)

            if len(result) == k:
                return result

        return result
