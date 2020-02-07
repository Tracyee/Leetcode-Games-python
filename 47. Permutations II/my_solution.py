class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        This is exactly the same as 46. Permutations,
        which utilize the algorithm in the nextPermutation
        '''
        nums.sort()
        ret = [nums.copy()]
        length = len(nums)
        while length > 1:
            i = length - 1
            while i > 0 and nums[i-1] >= nums[i]:
                i -= 1
            if i == 0 and nums[i] >= nums[i+1]:
                return ret
            else:
                j = i - 1
                while j < length-1 and nums[j+1] > nums[i-1]:
                    j += 1
                nums[i-1], nums[j] = nums[j], nums[i-1]
                nums[i:] = nums[i:][::-1]
                ret.append(nums.copy())
        return ret
