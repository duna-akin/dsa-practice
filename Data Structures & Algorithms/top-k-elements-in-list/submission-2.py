class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = dict()

        for num in nums:
            count[num] = count.get(num, 0) + 1

        # list of lists where the index of the list indicates the frequency of the nums in it
        freq = [[] for _ in range(len(nums) + 1)]

        for num, count in count.items():
            freq[count].append(num)

        
        # return top k 

        res = list()
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)

            if len(res) == k:
                return res

        return res
