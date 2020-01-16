class Solution:
    def maxSubArray(self, nums):
        '''
        input:
        - nums: list of integers
        output:
        - the sum of the contiguous subarray, which has the largest sum
        '''
        current_sum = 0
        best_sum = float('-inf')
        for idx in range(len(nums)):
            # if current_sum > 0:
            #     current_sum += nums[idx]
            # else:
            #     current_sum = nums[idx]
            current_sum = max(nums[idx], current_sum+nums[idx])
            # if current_sum > best_sum:
            #     best_sum = current_sum
            best_sum = max(best_sum, current_sum)
        return best_sum
