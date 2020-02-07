class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        used = []
        for i in range(len(nums)):
            if nums[i] not in used:
                self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
            used.append(nums[i])
