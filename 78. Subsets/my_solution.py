class Solution:
    def subsets(self, nums):
        n = len(nums)
        # nums.sort()
        subset = [[]]
        # for i in range(1, n+1):
        #     if i == 1:
        #         subset += [[j] for j in nums]
        #     if i == 2:
        #         subset += [[nums[j], nums[k]] for j in range(n) for k in range(j+1,n)]
        #     if i == 3:
        #         subset += [[nums[j], nums[k], nums[l]] for j in range(n) for k in range(j+1,n) for l in range(k+1,n)]
        # return subset
        
        from itertools import combinations
        for i in range(1, n+1):
            comb = combinations(nums, i)
            subset += [list(j) for j in comb]
        return subset
