class Solution:
    def permute(self, nums):
        def perm(k=0):
            if k == len(nums):
                ret.append(nums[:]) # or nums.copy()
                # print(ret)
            else:
                for i in range(k, len(nums)):
                    nums[k], nums[i] = nums[i] ,nums[k]
                    perm(k+1)
                    nums[k], nums[i] = nums[i], nums[k]
        ret=[]
        perm()
        return ret
