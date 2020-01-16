class Solution:
    def maxSubArray(self, nums):
        '''
        input:
        - nums: list of integers
        output:
        - the sum of the contiguous subarray, which has the largest sum
        '''
        largest_sum = nums[0]
        for i in range(len(nums)):
            for j in range(len(nums[i:])):
                if sum(nums[i:j+i+1]) > largest_sum:
                    largest_sum = sum(nums[i:i+j+1])
                    # print(str(nums[i:i+j+1]) + str(largest_sum))
        return largest_sum
