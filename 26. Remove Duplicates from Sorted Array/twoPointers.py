class Solution:
    def removeDuplicates(self, nums):
        '''
        input:
        - nums: sorted list of integers
        output:
        - the length of the new array
        '''
        slow_runner = 0 # pointer 1
        for i in range(len(nums)-1):
            if nums[slow_runner] != nums[i+1]: # i+1 is the fast_runner, i.e. pointer 2
                slow_runner += 1
                nums[slow_runner] = nums[i+1]
        return slow_runner + 1
