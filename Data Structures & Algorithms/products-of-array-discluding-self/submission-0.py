class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # genius solution

        # WE DON'T EVEN NEED THESE EXTRA ARRAYS
        # prefix = [nums[0]]
        # postfix = [nums[len(nums) - 1]]
        # compute prefix
        # for i in range(1, len(nums)):
        #     prefix.append(nums[i - 1] * nums[i])
        # # compute postfix
        # for i in range(len(nums) - 1, -1, -1):
        #     postfix.insert(0, nums[i - 1] * nums[i])
        # result[i] = prefix[i - 1] * postfix[i + 1]

        output = [1] * len(nums)
        prefix = 1

        # fill table prefix
        for i in range(0, len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        postfix = 1

        # fill table postfix
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output
        

