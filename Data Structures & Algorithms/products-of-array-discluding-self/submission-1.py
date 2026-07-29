class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # generate the result list
        result = [1] * len(nums)

        # keep track of prefix
        prefix = 1

        # slide through the array to fill list with prefix multiplications (multiplication of all nums before the curr num)
        for i in range(0, len(nums)):
            
            result[i] = prefix

            # compute prefix again for next num
            prefix = prefix * nums[i]

        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix

            postfix = postfix * nums[i]


        return result
        