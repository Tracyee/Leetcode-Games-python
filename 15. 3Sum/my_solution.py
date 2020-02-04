class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []
        l = len(nums)
        # if l < 3:
        #     return ans
        for i in range(l-2):
            if nums[i] > 0: break
            if i>0 and nums[i] == nums[i-1]: continue
            pnt1, pnt2 = i+1, l-1
            while pnt1 < pnt2:
                # print([pnt1, pnt2])
                three_sum = nums[i] + nums[pnt1] + nums[pnt2]
                if three_sum < 0:
                    pnt1 += 1
                elif three_sum > 0:
                    pnt2 -= 1
                elif three_sum == 0:
                    triplet = [nums[i], nums[pnt1], nums[pnt2]]
                    ans.append(triplet)
                    while pnt1 < pnt2 and nums[pnt1]==nums[pnt1+1]:
                        pnt1 += 1
                    while pnt1 < pnt2 and nums[pnt2]==nums[pnt2-1]:
                        pnt2 -= 1
                    pnt1 += 1
                    pnt2 -= 1
        return ans
