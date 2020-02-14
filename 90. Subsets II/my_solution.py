class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []
        n = len(nums)
        nums.sort()

        def helper(i, tmp):
            subset.append(tmp)
            # print(subset)
            for j in range(i, n):
                if j > i and nums[j] == nums[j-1]: continue
                helper(j + 1,tmp + [nums[j]] )
        helper(0, [])
        return subset
