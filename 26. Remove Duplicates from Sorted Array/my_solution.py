class Solution:
    def removeDuplicates(self, nums):
        '''
        input:
        - nums: sorted list of integers
        output:
        - the length of the new array
        '''
        del_count = 0
        for i in range(len(nums)-1):
            if nums[i-del_count] == nums[i-del_count+1]:
                del nums[i-del_count]
                # nums.pop(i-del_count)
                del_count += 1
        # return len(nums), nums
        return len(nums)

'''
Note that this implementation suffers from being inefficient,
as the del list[i] or list.pop(arbitrary_index_other_than_-1)
has O(n) time complexity
'''
