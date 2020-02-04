class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = len(nums)
        min_dist = float('inf')
        for i in range(l-2):
            # if i>0 and nums[i] == nums[i+1]: continue
            pnt1, pnt2 = i+1, l-1
            while pnt1 < pnt2:
                three_sum = nums[i] + nums[pnt1] + nums[pnt2]
                dist = abs(three_sum-target)
                if dist < min_dist:
                    min_dist = dist
                    closest_sum = three_sum
                #     print("closest sum is "+str(closest_sum))
                # print("three sum is "+str(three_sum))
                if three_sum - target < 0:
                    pnt1 += 1
                elif three_sum - target > 0:
                    pnt2 -= 1
                else:
                    return three_sum
                # while pnt1 < pnt2 and nums[pnt1] == nums[pnt1+1]:
                #     pnt1 += 1
                # while pnt1 < pnt2 and nums[pnt2] == nums[pnt2-1]:
                #     pnt2 -= 1
        return closest_sum
