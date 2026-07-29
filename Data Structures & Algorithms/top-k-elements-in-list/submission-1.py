class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # result array index: frequency, values: list of elements with that exact frequency; as a result we only need the the size of result array the exact same as input array

        # counting for number of times each value in nums (input array) occur
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # count will be the index
        for num, count in count.items():

            # append the num to the list in the specific count freq index
            freq[count].append(num)

        res = []

        # iterate in descending order
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
        
            if len(res) == k:
                break

        return res